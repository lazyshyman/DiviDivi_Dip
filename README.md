# DiviDivi_Dip
DiviDivi_Dip은 opencv를 이용하여 플레이어의 손 모양을 인식하고 해당 손 모양을 통해 일종의 참참참 게임을 진행하고 최대한 오래 버티는 것이 목표인 게임입니다.

## 시작하기

### 환경설정
먼저 캠을 사용할 수 있는 장치가 필요합니다.

### pip install
```python
pip install opencv
or
pip install opencv-python
```

```python
pip install mediapipe
```

```python
pip install numpy
```

```python
pip install pygame
```
## 게임 시작

필요한 모듈을 pip을 통해 모두 다운로드 받았다면 다음 코드를 실행하여 DiviDivi Dip을 실행합니다.
```python
python dividividip.py
```
## 게임 설명
DiviDivi_Dip을 모르는 사람을 위해 먼저 설명하자면 2000년대 예능프로그램에서 유행했던 한 게임이다. 참참참 게임의 일종으로 몸으로 참참참 게임을 진행하는 게임이다. 이 프로젝트는 간소화해서 몸으로 게임을 진행하지 않고 손으로 게임을 진행한다.
![ones_example](https://github.com/lazyshyman/DiviDivi_Dip/assets/125116906/f9056b0b-fbed-44b2-b669-f8a79dfa625e)
![rocks_example](https://github.com/lazyshyman/DiviDivi_Dip/assets/125116906/e5b7f80d-b0fc-48ea-9ec4-db4b4c89647e)
![image](https://github.com/lazyshyman/DiviDivi_Dip/assets/125116906/52ac3441-9140-4af5-81f8-5f1f4ac27722)


위의 각각 3가지 동작들(순서대로 one, rock, wing이라고 지칭)이 있고 컴퓨터가 선택하는 모양과 플레이어의 동작이 같지 않을 때까지 진행하는 게임으로 최대한 오래 버티는 것을 목표로 하는 게임이다.

### 게임 시작
#### 들어가기 앞서
이 게임은 게임을 start할 때에만 opencv가 작동되며 그 외에 작동은 모두 마우스로 처리합니다.


## 개발과정 및 기능설명
### 1. 메뉴 화면

#### 코드
```python
    screen.fill((255, 255, 255))
    #게임 화면 초기화
    bg_image.set_alpha(100)
    screen.blit(bg_image, (0, 0))
    game_name = creator_font.render('DiviDivi Dip', True, (0, 0, 0))
    # 제작자 이름 표시 위치 설정 (화면 중앙)
    text_rect = game_name.get_rect(center=(screen_width/2, screen_height/2 -50))
    screen.blit(game_name, text_rect)

    # 각 버튼에 대해 투명한 Surface를 그리고, 이를 화면에 blit
    for button in [start_button, creator_button, exit_button]:
        pygame.draw.rect(transparent_surface, (255, 255, 255, 0), button)  # 버튼 배경
        pygame.draw.rect(transparent_surface, (255, 255, 255, 0), button, 2)  # 버튼 테두리, 2는 테두리 두께
        screen.blit(transparent_surface, button.bottomright)

    # 버튼 텍스트 그리기
    for button, text in zip([start_button, creator_button, exit_button], ['Start', 'Creator', 'Exit']):
        text_surface = menu_font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button.center)
        screen.blit(text_surface, text_rect)

    # 이벤트 처리
    for event in pygame.event.get():#running 중 키보드나 마우스 입력값을 체크하는 것
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는지
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if start_button.collidepoint(mouse_pos):
                game_started = True
            elif creator_button.collidepoint(mouse_pos):
                display_creator = True
            elif exit_button.collidepoint(mouse_pos):
                running = False
            elif back_button.collidepoint(mouse_pos):
                display_creator = False
        elif event.type == TIMEREVENT:
            computer_hand_shape = random.choice(hand_shapes)
```

#### 세부사항
* start, creator, exit 버튼으로 이루어짐
* 각각 start는 게임을 시작하는 버튼이고, creator는 제작자를 표기하는 화면으로 넘어가는 버튼이고, exit는 시작화면에서 exit를 누르면 게임을 종료하는 버튼이다.

### 2. 게임 기능 구현
#### 코드
```python
if game_started:
        max_num_hands = 1
        gesture = {
            0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
            6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok'
        }
        rps_gesture = {0:'rock', 1:'one', 5:'paper', 8:'spiderman'}

        # MediaPipe hands model
        mp_hands = mp.solutions.hands
        mp_drawing = mp.solutions.drawing_utils
        hands = mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

        # Gesture recognition model
        file = np.genfromtxt('oss_project/data/gesture_train.csv', delimiter=',')
        angle = file[:,:-1].astype(np.float32)
        label = file[:, -1].astype(np.float32)
        knn = cv2.ml.KNearest_create()
        knn.train(angle, cv2.ml.ROW_SAMPLE, label)

        cap = cv2.VideoCapture(0)# 비디오 캡처 객체 생성

        while cap.isOpened():
            ret, img = cap.read()
            if not ret:
                continue

            img = cv2.flip(img, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            result = hands.process(img)

            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            if result.multi_hand_landmarks is not None:
                for res in result.multi_hand_landmarks:
                    joint = np.zeros((21, 3))
                    for j, lm in enumerate(res.landmark):
                        joint[j] = [lm.x, lm.y, lm.z]

                    # Compute angles between joints
                    v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
                    v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
                    v = v2 - v1 # [20,3]
                    # Normalize v
                    v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                    # Get angle using arcos of dot product
                    angle = np.arccos(np.einsum('nt,nt->n',
                        v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                        v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

                    angle = np.degrees(angle) # Convert radian to degree

                    # Inference gesture
                    data = np.array([angle], dtype=np.float32)
                    ret, results, neighbours, dist = knn.findNearest(data, 3)
                    idx = int(results[0][0])

                    # Draw gesture result
                    if idx in rps_gesture.keys():
                        user_hand_shape = rps_gesture[idx]#실시간을 플레이어의 손 모양 값
                        cv2.putText(img, text=rps_gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)


                    mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)
            cv2.imshow('Your_Hand', img)
            if not music_start:
                #Pygame mixer 초기화
                pygame.mixer.init()
                pygame.mixer.music.load('oss_project/audio/Youtube_Audio_Library_March_On.mp3')# 음악 로드
                pygame.mixer.music.play(-1)# 게임 시작 시 음악 재생
                music_start = True

            screen.fill((255, 255, 255))#게임 화면 초기화
            game_bg_image.set_alpha(100)
            screen.blit(game_bg_image, (0, 0))

            if not gameofgame_started:
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                if seconds <= 15:#게임시작 전 준비화면 보여주는 것
                    game1_text = creator_font.render("The Game starts in " + str(15-int(seconds)) + "seconds", True, (0, 0, 0))
                    text1_rect = game1_text.get_rect(center=(screen_width/2, screen_height/2 - 50))
                    game3_text = creator_font.render("Get ready your hand shape", True, (0, 0, 0))
                    text3_rect = game3_text.get_rect(center=(screen_width/2, screen_height/2 + 40))
                    screen.blit(game1_text, text1_rect)
                    screen.blit(game3_text, text3_rect)
                else:
                    if game_start_ticks is None:
                        game_start_ticks = pygame.time.get_ticks()
                    game_start_seconds = (pygame.time.get_ticks() - game_start_ticks) / 1000

                    if game_start_seconds <= 1:#game start 문구 1초 정도 보여주고 게임 진행
                        game2_text = creator_font.render("Game Start!", True, (0, 0, 0))
                        text_rect = game2_text.get_rect(center=(screen_width/2, screen_height/2 - 50))
                        screen.blit(game2_text, text_rect)
                    else:
                        if event.type == TIMEREVENT:
                            computer_hand_shape = random.choice(hand_shapes)
                            if computer_hand_shape == 'paper':
                                screen.blit(hand_images['wing'], (0,0))
                                if computer_hand_shape == user_hand_shape:
                                    game_over = True
                                else:
                                    current_score += 1
                            elif computer_hand_shape == 'one':
                                screen.blit(hand_images['one'], (0,0))
                                if computer_hand_shape == user_hand_shape:
                                    game_over = True
                                else:
                                    current_score += 1
                            elif computer_hand_shape == 'rock':
                                screen.blit(hand_images['rock'], (0,0))
                                if computer_hand_shape == user_hand_shape:
                                    game_over = True
                                else:
                                    current_score += 1                    
                if cv2.waitKey(1) == ord('q'):
                    break
                # 이벤트 처리
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는지
                        sys.exit()
            pygame.display.update()
```
#### 세부사항
* 3초마다 컴퓨터가 'one', 'rock', 'paper'중 한 가지를 택해서 화면에 보여주고 사용자와 처음 모양이 다르면 점수르 1점 추가한다. 만약 컴퓨터가 선택한 모양과 사용자의 손모양이 같으면 게임은 종료된다.

### 3. Creator
#### 코드
```python
if display_creator:
        screen.fill((255, 255, 255))  #새로운 화면 흰색으로 설정
        # 제작자 이름 표시
        creator_name = creator_font.render('Creator: 20101219 Kimjunsoo', True, (0, 0, 0))
        # 제작자 이름 표시 위치 설정 (화면 중앙)
        text_rect = creator_name.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(creator_name, text_rect)

        # 뒤로가기 버튼 위치 설정
        screen.blit(back_button_image, back_button.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button.collidepoint(mouse_pos):
                    display_creator = False  # 뒤로가기 버튼을 누르면 제작자 화면에서 벗어남
        pygame.display.update()
```
#### 세부사항
* 뒤로가기 버튼을 누르면 초기화면으로 돌아감
* 제작자 이름 화면 가운데 표기

### 4. 게임 종료
#### 코드
```python
if game_over:
        game_started = False
        pygame.mixer.music.stop()
        screen.fill((255, 255, 255))#게임 화면 초기화
        game_bg_image.set_alpha(100)
        screen.blit(game_bg_image, (0, 0))
        final_score = current_score
        current_score = 0
        score_text = creator_font.render("Your score: " + str(final_score) + "times", True, (0, 0, 0))
        text_rect = score_text.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(score_text, text_rect)

        # 뒤로가기 버튼 위치 설정
        screen.blit(back_button_image, back_button.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button.collidepoint(mouse_pos):
                    game_started = False

        pygame.display.update()    
```
#### 세부사항
* 게임종료 시 사용자가 그동안 버틴 횟수를 점수로 표시해준다.


## 개발환경 및 실행환경
Python 3.11.2 (Window 11), VsCode 사용

## 데모영상
https://github.com/lazyshyman/DiviDivi_Dip/assets/125116906/03ed4ce2-2aa2-486f-984e-0a4fe6dd049c


## 마치며
아쉬운점 : 게임을 완성시키지 못한 것이 매우 아쉽다. 좀 더 공부해서 원하던 게임으로 완성할 수 있어야 할 것 같다...추가로 나중에 다른 dataset을 이용하여 opencv를 활용한 다른 손모양의 인식률을 높여 다른 손모양으로 해볼 수 있으면 좋을 거 같다라는 생각을 했다.
