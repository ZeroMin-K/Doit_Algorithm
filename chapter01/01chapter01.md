# Chapter 01 알고리즘 기초 

1. 알고리즘 이란?

  * 세 정수의 최댓값 
    * 문자열과 숫자 입력받기 `input(문자열)`
    * 복합문의 구조 

> 알고리즘
: 어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차
>> 올바른 알고리즘
: 어떠한 경우에도 실행결과가 똑같이 나오는 것 


  * 세 정수의 대소 관계 나열 => 결정 트리 
  * 조건문과 분기
    ```python
    if ( **b >= a** and c <= a) or (**b <= a** and c >= a):
    elif (**a > b** and c < b) or (**a < b**) and c >b):
    ```
    a와 b를 여러번 비교 => 비효율적
  * 순서도

2. 반복하는 알고리즘
  * while, for 반복
  * range()함수로 이터러블 객체 생성 
  * 값 교환 => 튜플 이용     ` a, b = b, a `
  * 반복 과정 중 반복 횟수가 상당히 큰 수 일 때 비효율적
     * +,-을 번갈아 출력하는 예제 
   ```python
  for i in range(1, n + 1):
    if i % 2:
      print('+', end='')
    else:
      print('-', end='')
  ```
  
  n이 커질수록 if문 조건 확인 또한 여러번 수행 => 비효율적
  
  ```python
  for _in range(n //2):
    print('+-', end='')
  if n % 2:
    print('+', end='')
   ```
  
  짝수인 경우, n의 절반만큼만 수행. 홀수인 경우, n의 절반과 마지막 if문 수행
  
  * 반복에서 break, continue
    - while문, for문이 종료된 후 카운터용 변수 값
  * 반복문 건너뛰기, 여러범위 스캔
  * 비교 연산자를 연속으로 사용 `10 <= no <= 90`
  * 드모르간의 법칙
  * 다중 루프
  * 파이썬의 변수 

  
  
