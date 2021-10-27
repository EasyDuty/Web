# EasyDuty web



# 환경

python 3. 9. 6

django 3. 2. 7



# models & forms

AbstractUser을 상속받아 유저 모델을 간호사 모델로 이용

유저 모델의 필드는 회원가입 때 사용할 NurseForm, 

회원 정보 변경 떄 사용할 NurseChangeForm을 구현했다.



## 해야하는 것

Duty 생성 페이지 구현

관리자 - 병동 당 한 명, 여러 팀 Duty를 생성해야함(어떤 값을 입력받아야 하는가?)

오프 신청 받으면 처리 구현



# 문제점 & 해결법

* AbstractUser에 상속받은 필드는 한글로 번역되어 통일성이 떨어짐

  forms.py에서 label을 이용해 나머지 필드도 한글로 출력해줌

* Date picker 구현

  다양한 방법이 있는데, 일단 jquery의 datepicker을 이용하여 widget으로 구현.

  django-datepicker도 있던데 어떤 것을 사용할지 고민해 봐야할 듯

* Date picker과 자동완성이 같이 나오는 문제.

  setAttribute('autocomplete', 'off') 을 통해 해결.
  
  