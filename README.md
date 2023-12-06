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

위의 각각 3가지 동작들(순서대로 one, rock, wing이라고 지칭)이 있고 컴퓨터가 선택하는 모양과 플레이어의 동작이 같지 않을 때까지 진행하는 게임으로 최대한 오래 버티는 것을 목표로 하는 게임이다.

### 게임 시작

1. cam에 손을 비추어 에임(핑크색 포인터)이 손을 잘 따라오는지 확인합니다.
2. Start! 버튼에 '발사' 동작을 취해 난이도 선택화면으로 넘어갑니다.
3. 난이도를 선택 후 표적들을 '발사' 합니다.


## 개발과정 및 기능설명

### 1.

#### 코드

#### 세부사항
* 

### 2. 메뉴 화면


#### 코드

#### 세부사항
* 


### 3. 게임 기능 구현


#### 코드

#### 세부사항
* 

### 4.
#### 코드
```
#### 세부사항
* 

### 7. 스코어보드

#### 코드
```       
```
#### 세부사항
* 배경 추가 - 12월 20일 추가
* 메뉴화면으로 돌아가기 - 12월 20일 추가


## 개발환경 및 실행환경

Python 3.11.2 (Window 11), VsCode 사용


## 데모영상


실제 DiviDivi_Dip 작동시 cam 은 출력되지 않습니다. 

### cam 출력을 원할시 코드 수정 
```python
# cv2.imshow('Game', img)
```
줄의 주석을 해제 하면 됩니다.


## 마치며
아쉬운점 : 원래 계획은 openpose모듈을 이용하여 플레이어의 전체 몸을 인식한 진짜 디비디비딥 게임을 만들어보고 싶었으나, openpose모듈이 다운로드 하는 과정에서 계속 오류가 생겨 openpose모듈을 이용할 수 없었다. 나중에는 openpose모듈을 이용하여 진짜 DiviDivi_Dip게임을 만들어보고 싶다.

