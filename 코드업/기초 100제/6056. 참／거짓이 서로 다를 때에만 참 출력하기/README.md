# [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py) - 6056

[문제 링크](https://codeup.kr/problem.php?id=6056)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-논리연산

### 채점결과

정확한 풀이

### 문제 설명

본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;<br />
------ <br />
<br />
2개의 정수값이 입력될 때&#44; <br />
그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.<br />
<br />
예시 <br />
... <br />
c = bool(int(a)) <br />
d = bool(int(b)) <br />
print((c and (not d)) or ((not c) and d)) <br />
<br />
참고<br />
참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or&#44; 배타적 논리합) 연산이라고도 부른다. <br />
<br />
논리연산자는 사칙(+&#44; -&#44; *&#44; /) 연산자와 마찬가지로 여러 번 중복해서 사용할 수 있는데&#44;&nbsp; <br />
사칙 연산자와 마찬가지로 계산 순서를 표시하기 위해 괄호 ( )를 사용할 수 있다. <br />
괄호를 사용하면 계산 순서를 명확하게 표현할 수 있다. <br />
<br />
수학 식에서는 소괄호 ()&#44; 중괄호 {}&#44; 대괄호 []를 사용하기도 하지만&#44; 프로그래밍언어에서는 소괄호 ( ) 만 사용한다. <br />
<br />
** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다. <br />
<p style="text-align:right;">
	<img src="/admin/../upload/pimg6221_1.png" alt="" /> 
<br />

### 입력

2개의 정수가 공백을 두고 입력된다.<br />
<br />

### 출력

두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고&#44; 그 외의 경우에는 False 를 출력한다.<br />
<br />

### 입력 예시

<pre>1 1</pre>

### 출력 예시

<pre>False</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
