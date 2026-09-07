# [기초-논리연산] 참 거짓 바꾸기(설명)(py) - 6053

[문제 링크](https://codeup.kr/problem.php?id=6053)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-논리연산

### 채점결과

정확한 풀이

### 문제 설명

<span>본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;</span><br />
<span>------</span><br />
<br />
정수값이 입력될 때&#44; <br />
그 불 값을 반대로 출력하는 프로그램을 작성해보자. <br />
<br />
예시 <br />
a = bool(int(input()))<br />
print(not a)<br />
<br />
참고<br />
<span>a = bool(int(input()))</span> <br />
<span>와 같은 형태로 겹쳐 작성하면&#44; 한 번에 한 단계씩 계산/처리/평가된다.</span> <br />
<span>위와 같은 명령문의 경우 input( )&#44; int( )&#44; bool( ) 순서로 한 번에 한 단계씩 계산/처리/평가된다.</span> <br />
<br />
어떤 불 값이나 변수에 not True&#44; not False&#44; not a 와 같은 계산이 가능하다. <br />
<br />
참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word&#44; keyword)를 사용할 수 있다.<br />
<br />
이러한 논리연산을 NOT 연산(boolean NOT)이라고도 부르고&#44; <br />
프라임 '(문자 오른쪽 위에 작은 따옴표)&#44; 바(기호 위에 가로 막대)&#44; 문자 오른쪽 위에 <sup>c</sup>(여집합&#44; complement)&nbsp;등으로 표시한다. <br />
모두 같은 의미이다. <br />
<br />
<span>참&#44; 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not&#44; and&#44; or 이 있고&#44;</span><br />
<span>불 값들 사이의 논리(not&#44; and&#44; or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산 된다.</span><br />
<br />
정수값 0은 False 이고&#44; 나머지 정수 값들은 True 로 평가된다. <br />
빈 문자열 "" 나 ''는 False 이고&#44; 나머지 문자열들은 True 로 평가된다. <br />
<br />
** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다. <br />
<p style="text-align:right;">
	<img src="/admin/../upload/pimg6218_1.png" alt="" /> <br />
<br />
<br />

### 입력

정수 1개가 입력된다. <br />
<br />

### 출력

입력된 정수의 불 값이 False 이면 True&#44; True 이면 False 를 출력한다. <br />
<br />

### 입력 예시

<pre>1</pre>

### 출력 예시

<pre>False</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
