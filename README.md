# 패치노트

## 11/04

* get_duty url & view함수 생성 - get_duty(request, username, year, month)
* static 설정 추가

## 11/01

* user model 구조 변경

  is_manager 추가, duty를 jsonfield로 변경 - 이에 따른 main 출력 구조 변경

  달력을 통해 원하는 날짜로 이동할 수 있어야하는데, 일단은 현재 날짜에 해당하는 달로 출력

* nav 바에서 듀티 생성이 POST로 되어있던 것 GET으로 수정

## 10/27

* date picker 추가

  jquery의 date picker 이용

* 기본 기능 구현 완료 - 1인 일 때 v1.0

## 10/26

* 통일성을 위해 form labeling으로 한글이름으로 바꿔 줌

## 10/25

* 알고리즘 추가 (1인)
* 비밀번호 변경 기능 추가
* 프로필 페이지 추가

## 10/20

* 모델 구조 변경 

  나이 -> 생일, 경력 -> 입사일 : 계산 편의성을 위해

## 10/19

* user - 커스텀 유저 모델로 대체, Nurse 모델 대신 커스텀 유저 모델을 이용
* 오프 신청 모델, 폼 구현 : 알고리즘이 추가되면 추가

## 10/3

* 기본 기능 추가 - 모델, 폼, 회원가입, 로그인, 로그아웃, 회원정보 수정 등등



---



# EasyDuty web 1.0

* 한 명의 간호사가 존재할 때 듀티 생성
* jquery를 이용하여 date picker 구현
* 현재 마지막 이틀의 듀티, 년도, 월을 입력받아 듀티 생성 - 처음에만 필요한 정보이므로 수정 필요
* main templates 수정 필요
* 여러 명으로 확장 시 off 신청 구현 필요



---



# 환경

python 3. 9. 6



# models & forms

AbstractUser을 상속받아 유저 모델을 간호사 모델로 이용

유저 모델의 필드는 회원가입 때 사용할 NurseForm, 

회원 정보 변경 떄 사용할 NurseChangeForm을 구현했다.



## 해야하는 것

* 관리자 - 병동 당 한 명, 여러 팀 Duty를 생성해야함(어떤 값을 입력받아야 하는가?)

  일단 회원가입시 is_manager 필드를 추가하여 해결하면 될 듯

* 오프 신청 받으면 처리 구현

* duty 생성 시 팀원 선택

* 팀 듀티 확인 - 같은 팀원의 듀티를 볼 수 있도록

  team=request.user.team을 통해 같은 팀원을 골라오고, 해당하는 달에 duty를 꺼내오면 될 듯.
  
  

---



# 문제점 & 해결법

* duty는 간호사당 년-월 별로 따로 저장되어 있어서 확인할 수 있어야함.

  django에서 제공하는 jsonfield를 이용하여 해결.

  2021년 11월 듀티라고 하면, 키값으로 202111로 저장, 만약 이 때 듀티가 존재한다면, 메인에서 출력할 수 있도록 함 

* AbstractUser에 상속받은 필드는 한글로 번역되어 통일성이 떨어짐

  forms.py에서 label을 이용해 나머지 필드도 한글로 출력해줌

* Date picker 구현

  다양한 방법이 있는데, 일단 jquery의 datepicker을 이용하여 widget으로 구현.

  django-datepicker도 있던데 어떤 것을 사용할지 고민해 봐야할 듯

* Date picker과 자동완성이 같이 나오는 문제.

  setAttribute('autocomplete', 'off') 을 통해 해결.

  

  