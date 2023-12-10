# DiviDivi_Dip
DiviDivi_Dip은 opencv를 이용하여 플레이어의 손 모양을 인식하고 해당 손 모양을 통해 일종의 참참참 게임을 진행하고 최대한 오래 버티는 것이 목표인 게임입니다.

##

##시작하기

###환경설정
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
####들어가기 앞서
이 게임은 게임을 start할 때에만 opencv가 작동되며 그 외에 작동은 모두 마우스로 처리합니다.


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

