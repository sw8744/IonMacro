# Ion 노트북실 자리예약 매크로
~~(창운아 미안)~~
## 개요
요즘 수행 기간이라 노트북실 자리가 매우 부족한 상황이다. 그래서 예약의 편리성을 증가시키기 위해 매크로를 제작하기로 결심하였다.

## 사용법
main.py에 들어가서, 변수 설정이라 써 있는 부분 밑에 주석 달린 그대로 적고 실행하기만 하면 된다.

당연히, 컴퓨터에 Python은 깔려 있어야 한다.

## 대략적인 작동 원리
- Selenium을 통해 Ion 페이지에 접속한다.
- 자동으로 로그인을 계속 진행한다.
- 로그인이 되었으면 /ns 를 쳐서 면불 예약 페이지로 이동한다.
- 앞서 적었던 장소, 선생님, 신청사유를 자동으로 입력한다.
- 면불 시간 별로 자동으로 노트북실 빈 자리를 찾아 예약을 시도한다.