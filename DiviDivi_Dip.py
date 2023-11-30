import cv2
import mediapipe as mp
import numpy as np
import pygame, random, sys, os

# MediaPipe 손 인식 초기화
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#Pygame 초기화
pygame.init()

#점수 설정
score = 0
final_score = 0

# 게임 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dividivi_Dip")


# 배경 이미지 로드
bg_image = pygame.image.load('images/start_background.png')
#게임배경 이미지 로드
game_bg_image = pygame.image.load('images/game_background.png')
game_bg_image = pygame.transform.scale(game_bg_image, (screen_width, screen_height))
# 뒤로가기 버튼 이미지 로드
back_button_image = pygame.image.load('images/back_button.png')
# 뒤로가기 버튼 이미지 크기 조절
back_button_image = pygame.transform.scale(back_button_image, (35, 35))

# 가위, 바위, 보 이미지 로드 및 화면 크기에 맞게 조절
hand_images = {
    'rock': pygame.transform.scale(pygame.image.load('images/rocks.png'), (screen_width, screen_height)),
    'one': pygame.transform.scale(pygame.image.load('images/ones.png'), (screen_width, screen_height)),
    'wings': pygame.transform.scale(pygame.image.load('images/wings.png'), (screen_width, screen_height)),
}

# 손 모양 리스트
hand_shapes = ['rock', 'one', 'wings']

# 타이머 이벤트 타입 설정
TIMEREVENT = pygame.USEREVENT + 1

# 타이머 설정 (2초마다 이벤트 발생)
pygame.time.set_timer(TIMEREVENT, 3000)

def get_hand_shape(hand_landmarks):
    # 각 손가락의 끝 부분
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # 각 손가락의 MCP(손바닥과 연결된 부분)
    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
    index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    ring_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]
    pinky_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]

    # 각 손가락이 접혀 있는지 판단
    thumb_folded = thumb_tip.y > thumb_mcp.y
    index_finger_folded = index_finger_tip.y > index_finger_mcp.y
    middle_finger_folded = middle_finger_tip.y > middle_finger_mcp.y
    ring_finger_folded = ring_finger_tip.y > ring_finger_mcp.y
    pinky_folded = pinky_tip.y > pinky_mcp.y

    # 'rock', 'paper', 'scissors' 판단
    if thumb_folded and index_finger_folded and middle_finger_folded and ring_finger_folded and pinky_folded:
        return 'rock'
    elif thumb_folded and not index_finger_folded and middle_finger_folded and ring_finger_folded and pinky_folded:
        return 'one'
    elif not thumb_folded and index_finger_folded and middle_finger_folded and ring_finger_folded and not pinky_folded:
        return 'wings'
    else:
        return None

# 웹캠에서 이미지를 캡처합니다.
cap = cv2.VideoCapture(0)

# 게임 시작 버튼
start_button = pygame.Rect(screen_width-100, screen_height-140, 100, 50)
# 제작자 정보 버튼
creator_button = pygame.Rect(screen_width-100, screen_height-100, 100, 50)
# 게임 종료 버튼
exit_button = pygame.Rect(screen_width-100, screen_height-60, 100, 50)
# 뒤로가기 버튼 위치 설정
back_button = pygame.Rect(20, screen_height-50, 100, 50)

# 투명한 Surface 생성
transparent_surface = pygame.Surface((100, 50), pygame.SRCALPHA)

# 폰트 설정
menu_font = pygame.font.SysFont('arial', 30)
creator_font = pygame.font.SysFont('arial', 50)
creator_font.set_bold(True)

running = True
game_started = False
display_creator = False

while running:
    #게임 화면 초기화
    screen.blit(bg_image, (0, 0))

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
        

    if display_creator:
        creator_screen = pygame.display.set_mode((screen_width, screen_height))  # 새로운 화면 크기 설정
        creator_screen.fill((0, 0, 0))  # 새로운 화면 배경색 설정
        # 제작자 이름 표시
        creator_name = creator_font.render('Creator: 20101219 Kimjunsoo', True, (255, 255, 255))
        # 제작자 이름 표시 위치 설정 (화면 중앙)
        text_rect = creator_name.get_rect(center=(screen_width/2, screen_height/2))
        creator_screen.blit(creator_name, text_rect)

        # 뒤로가기 버튼 그리기
        creator_screen.blit(back_button_image, back_button.bottomleft)
        pygame.display.flip()  # 화면 업데이트
        continue  # 제작자 이름 화면 표시 중에는 아래 게임 로직을 실행하지 않음

    if game_started:
        game_screen = pygame.display.set_mode((screen_width, screen_height))  # 새로운 게임 화면 생성
        game_screen.bilt(game_bg_image, (0,0))#게임 화면 초기화
        if event.type == TIMEREVENT:
            # 웹캠에서 이미지 캡처
            ret, frame = cap.read()
            if not ret:
                continue
            # 이미지를 RGB로 변환하고 손 모양 인식
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = mp_hands.Hands().process(image)
            # 게임이 가위, 바위, 보 중 하나를 랜덤으로 선택
            computer_hand_shape = random.choice(hand_shapes)
            if computer_hand_shape == 'wings':
                game_screen.blit(hand_images['rock'], (0,0))
            elif computer_hand_shape == 'ones':
                game_screen.blit(hand_images['one'], (0,0))   
            elif computer_hand_shape == 'rocks':
                game_screen.blit(hand_images['wing'], (0,0))
            # 플레이어의 손 모양 판단
            user_hand_shape = None
            # 손 모양 인식에 사용
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    user_hand_shape = get_hand_shape(hand_landmarks)
                    pass

            # 사용자의 손 모양과 게임 화면의 손 모양 비교
            if user_hand_shape == computer_hand_shape:
                # 손 모양이 같으면 게임 종료
                running = False  
                # "Game over!" 텍스트 표시
                game_over_text = menu_font.render('Game over!', True, (255, 255, 255))
                game_screen.blit(game_over_text, (screen_width//2, screen_height//2))
            else:
                # 손 모양이 다르면 맞춘 횟수 증가
                score += 1
            pygame.display.update()

    # 게임 화면 업데이트
    pygame.display.update()

# 게임 종료
cap.release()
pygame.quit()



# with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             continue

#         # RGB로 변환합니다.
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = hands.process(image)

#         # 손이 감지되면 그림을 그립니다.
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
#         cv2.imshow('Hand Tracking', frame)
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break






