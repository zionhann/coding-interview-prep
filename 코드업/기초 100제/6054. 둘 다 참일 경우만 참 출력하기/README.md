# [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py) - 6054

[문제 링크](https://codeup.kr/problem.php?id=6054)

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
2개의 정수값이 입력될 때&#44; <br />
그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자. <br />
<br />
예시<br />
a&#44; b = input().split()<br />
print(bool(int(a)) and bool(int(b))) <br />
<br />
참고<br />
and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고&#44; 나머지 경우는 False 로 계산한다.<br />
이러한 논리연산을 AND 연산(boolean AND)이라고도 부르고&#44; · 으로 표시하거나 생략하며&#44;&nbsp;집합 기호 ∩(교집합&#44; intersection)로 표시하기도 한다.&nbsp; <br />
모두 같은 의미이다. <br />
<br />
참&#44; 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not&#44; and&#44; or 이 있고&#44;<br />
불 값들 사이의 논리(not&#44; and&#44; or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산된다. <br />
<br />
** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다. <br />
<p style="text-align:right;">
	<img src="/admin/../upload/pimg6219_1.png" alt="" /> <br />
<br />
<br />
<br />

### 입력

2개의 정수가 공백을 두고 입력된다. <br />
<br />

### 출력

둘 다 True 일 경우에만 True 를 출력하고&#44; 그 외의 경우에는 False 를 출력한다. <br />
<br />

### 입력 예시

<pre>1 1</pre>

### 출력 예시

<pre>True</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
