# DiviDivi_Dip
DiviDivi_Dip은 opencv를 이용하여 플레이어의 손 모양을 인식하고 해당 손 모양을 통해 일종의 참참참 게임을 진행하고 최대한 오래 버티는 것이 목표인 게임입니다.

##

##시작하기

###환경설정
캠을 연결합니다.

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
## 어플리케이션 시작

필요한 모듈을 pip을 통해 모두 다운로드 받았다면 다음 코드를 실행하여 DiviDivi Dip을 실행합니다.
```python
python dividividip.py
```
## 게임 설명
DiviDivi_Dip을 모르는 사람을 위해 먼저 설명하자면 2000년대 예능프로그램에서 유행했던 한 게임이다. 참참참 게임의 일종으로 몸으로 참참참 게임을 진행하는 게임이다. 이 프로젝트는 간소화해서 몸으로 게임을 진행하지 않고 손으로 게임을 진행한다.
![ones_example](https://github.com/lazyshyman/DiviDivi_Dip/assets/125116906/f9056b0b-fbed-44b2-b669-f8a79dfa625e)
![rocks_example](https://github.com/lazyshyman/DiviDivi_Dip/assets/125116906/e5b7f80d-b0fc-48ea-9ec4-db4b4c89647e)
![wings_example](https://github.com/lazyshyman/DiviDivi_Dip/assets/125116906/5d70c66c-c7c2-437d-9649-11c4182bb9af)
위의 3가지 동작이 있고 컴퓨터가 선택하는 모양과 플레이어의 동작이 같지 않을 때까지 진행하는 게임으로 최대한 오래 버티는 것을 목표로 하는 게임이다.

### 게임 시작

1. cam에 손을 비추어 에임(핑크색 포인터)이 손을 잘 따라오는지 확인합니다.
2. Start! 버튼에 '발사' 동작을 취해 난이도 선택화면으로 넘어갑니다.
3. 난이도를 선택 후 표적들을 '발사' 합니다.


## 개발과정 및 기능설명

### 1. 약지 손가락 두번째 마디를 에임으로 설정 (11월 26일 추가)

![image](https://user-images.githubusercontent.com/39877181/146876810-0bedaa35-5034-4644-b79b-8e60efc8d80b.png)

#### 코드
```python
px = joint[14][0] * (WINDOW_SIZE_WIDTH) + 0
py = joint[14][1] * (WINDOW_SIZE_HEIGHT) + 0
jointpos = [px,py]
if START_GAME > 0:
    if idx in aim_color.keys():
        pygame.draw.circle(windowSurface, aim_color[idx], jointpos,5)
        pygame.draw.circle(windowSurface, BLACK, (px,py), 20, 2)
        pygame.draw.line(windowSurface, BLACK, (px, py + 20, (px, py - 20), 2)
        pygame.draw.line(windowSurface, BLACK, (px + 20, py), (px - 20, py), 2) 
else:
    windowSurface.blit(pointerImage, jointpos)
```
#### 세부사항
* 손모양에 따라 다른 색깔을 맵핑
* 에임의 모양을 게임시작 후에는 저격 모양으로, 메뉴화면에서는 포인터 모양으로 설정.

### 2. 메뉴 화면

![image](https://user-images.githubusercontent.com/39877181/146876881-3e4a63cf-b502-4091-8072-d21189a7cfb4.png)

#### 코드
```python
def Menu():
    windowSurface.fill(WHITE)
    global MODE
    bg_trans = pygame.transform.scale(bg, (WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT))
    bg_trans.set_alpha(100)
    windowSurface.blit(bg_trans, [0,0])
    if MODE == 0:
        menuUI = []
        menuUI.append(pygame.Rect(320,300,100,40))
        menuUI.append(pygame.Rect(320,350,100,40))
        menuUI.append(pygame.Rect(320,400,100,40))

        # for rect in menuUI: #굳이 그릴필요 없음
        #     pygame.draw.rect(windowSurface, WHITE, rect)

        drawText("Eagle Hunt", windowSurface, 150, 130, FONT , BLACK) # 게임 이름

        uiname = ["Start!", "Creator", "Exit"]
        ui_y = [310,360,410]
        for idx in range(0,3):
            if menuUI[idx].collidepoint(jointpos):
                drawText(uiname[idx], windowSurface, 357,  ui_y[idx]-3, UIFONT2 , BLACK)
                if bang() == True:
                    MODE = idx+1
                    print(MODE)
            else:
                drawText(uiname[idx], windowSurface, 360, ui_y[idx], UIFONT , BLACK)
    if MODE == 1:
        SetDiffi()
    elif MODE == 2:
        Creator()
    elif MODE == 3:
        sys.exit()
```

#### 세부사항
* 메뉴 배경 추가 - 12월 20일 추가
* UI에 포인터 올라가면 UI글씨가 확대되는 효과 추가 - 12월 20일 추가
* Start! 를 bang할시 난이도 조절, Creator을 bang할시 이름출력, Exit을 bang할시 나가기 추가 - 12월 20일 추가

### 3. 난이도 선택

![image](https://user-images.githubusercontent.com/39877181/146876944-aab2b21c-3e3e-4fc1-adbc-3c22f042cc1a.png)

#### 코드
```python
def SetDiffi():
    difficultyRects = []
    difficultyRects.append(pygame.Rect(195, 95, 100, 40)) # difficultyRects.append(pygame.Rect(5, 450, random.randrange(100,200), 100))
    difficultyRects.append(pygame.Rect(195, 205, 120, 40))
    difficultyRects.append(pygame.Rect(195, 330, 100, 40))
    # for rect in difficultyRects:
    #    pygame.draw.rect(windowSurface, GREEN, rect)
    global START_GAME
    diffi_y = [95,210,335] # 난이도에 에임올려져 있을 시 강조 효과 추가
    for idx in range(1,4):
        if difficultyRects[idx-1].collidepoint(jointpos):
            drawText(GAME_MODE[idx], windowSurface, 197, diffi_y[idx-1]-3, DIFFIFONT2 , BLACK)
            if bang() == True:
                START_GAME = idx
        else:
            drawText(GAME_MODE[idx], windowSurface, 200, diffi_y[idx-1], DIFFIFONT , BLACK)

    Make_back()
```
#### 세부사항
* 
*
* 

### 4. 게임 기능 구현

![image](https://user-images.githubusercontent.com/39877181/146876996-f98f6fdc-c9a3-4112-b968-8590dccc66ea.png)
![image](https://user-images.githubusercontent.com/39877181/146877026-7bf6dcf6-7d95-474b-86c4-2f1a78724ee4.png)

#### 코드
```python
def game(): #211130 수정
    
    bg_trans = pygame.transform.scale(bg_game, (WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT))
    bg_trans.set_alpha(100)
    windowSurface.blit(bg_trans, [0,0])

    global START_GAME,total_target,score,frameNum
    if START_GAME == 4:
        ScoreBoard()
    elif START_GAME > 0:
        windowSurface.blit(backImage, [465, 465])
        makeTarget(GAME_MODE[START_GAME])
        if total_target == 0:
            while total_target < START_GAME * 2:        
                #targets.append((random.randrange(0,WINDOW_SIZE_WIDTH-TARGET_SIZE)
                #, random.randrange(0,WINDOW_SIZE_HEIGHT-TARGET_SIZE)))
                targets.append(pygame.Rect(random.randrange(0,WINDOW_SIZE_WIDTH - TARGET_SIZE),
                random.randrange(0,WINDOW_SIZE_WIDTH - TARGET_SIZE),TARGET_SIZE,TARGET_SIZE))
                total_target = total_target + 1

        backRect = pygame.Rect(465, 465, BACK_SIZE, BACK_SIZE)
        drawText("SCORE : ", windowSurface, 10,10, UIFONT , BLACK)
        drawText(str(score), windowSurface, 120,10, UIFONT , BLACK)


        if bang() == True:
            if backRect.collidepoint(jointpos):
                global finalScore
                finalScore = score
                targets.clear()
                total_target = 0
                score = 0
                START_GAME = 4
            for target in targets:
                if target.collidepoint(jointpos):
                    targets.remove(target)
                    score = score + START_GAME
                    total_target = total_target - 1

        frameNum = drawTarget(frameNum)
    
    else:
        #게임 시작이 아니면 메뉴 화면
        Menu()
```

#### 세부사항
* 게임 배경 설정 - 12월 20일 추가
* 게임이 시작했으면 타겟 만들기 - 11월 27일 추가
* 뒤로가기 버튼 추가 - 11월 30일 추가
* 게임 시작이 아니라면 메뉴화면
* 뒤로가기 버튼에 총을 쏘는 모션을 하면 점수화면 - 12월 20일 추가
* 타겟을 쏘면 타겟 사라지기 - 11월 27일 추가


### 6. bang (총을 쏘는 모션)
#### 코드
```python
def bang():
    global buffer
    if (buffer == 9 or buffer == 1 or buffer == 3) and (idx == 6 or idx == 0):
        return True
    else:
        buffer = idx
        return False
```
```python
gesture = {
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok',
}

# 특정한 제스쳐들만 사용하므로 인식률을 높이기 위해 다른 모양들도 주먹,가위에 추가해줌
rps_gesture = {6:'rock', 5:'paper', 9:'scissors', 1:'scissors', 0: 'rock', 3:'scissors'}
```

#### 세부사항
* 버퍼에 이전 손모양을 저장하여 (가위 모양 -> 주먹모양)으로 변경시 True 리턴 - 11월 26일 추가
* 대기하는 손 모양과 쏘는 손모양의 제스쳐들을 모두 유효 제스쳐로 추가 - 11월 26일 추가

### 7. 스코어보드

![image](https://user-images.githubusercontent.com/39877181/146877245-694fe203-5adf-4a2b-ba47-5591dffb874c.png)

#### 코드
```       
```
#### 세부사항
* 배경 추가 - 12월 20일 추가
* 메뉴화면으로 돌아가기 - 12월 20일 추가


## 개발환경 및 실행환경

Python 3.11.2 (Window 11), VsCode 사용


## 데모영상

https://user-images.githubusercontent.com/39877181/146882727-0e9b86b2-5b9c-467c-afe1-f2f6de9e6fee.mp4

실제 Eagle_Hunt 작동시 cam 은 출력되지 않습니다. 

### cam 출력을 원할시 코드 수정 
```python
# cv2.imshow('Game', img)
```
339줄의 주석을 해제 하면 됩니다.


## 마치며
아쉬운점 : 원래 계획은 openpose모듈을 이용하여 플레이어의 전체 몸을 인식한 진짜 디비디비딥 게임을 만들어보고 싶었으나, openpose모듈이 다운로드 하는 과정에서 계속 오류가 생겨 openpose모듈을 이용할 수 없었다. 나중에는 openpose모듈을 이용하여 진짜 DiviDivi_Dip게임을 만들어보고 싶다.

