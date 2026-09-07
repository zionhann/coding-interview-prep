# [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py) - 6063

[문제 링크](https://codeup.kr/problem.php?id=6063)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-3항연산

### 채점결과

정확한 풀이

### 문제 설명

<span>본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;</span><br />
<span>------</span><br />
<br />
입력된 두 정수(a&#44; b) 중 큰 값을 출력하는 프로그램을 작성해보자. <br />
단&#44; 3항 연산을 사용한다.<br />
<br />
예시 <br />
a&#44; b = input().split() <br />
a = int(a)&nbsp; #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장 <br />
b = int(b) <br />
c = (a if (a&gt;=b) else b) <br />
print(int(c))<br />
<br />
참고<br />
3개의 요소로 이루어지는 3항 연산은 <br />
"x if C else y" 의 형태로 작성이 된다. <br />
- C : True 또는 False 를 평가할 조건식(conditional ex<x>pression) 또는 값 <br />
- x : C의 평가 결과가 True 일 때 사용할 값<br />
- y : C의 평가 결과가 True 가 아닐 때 사용할 값<br />
<br />
조건식 또는 값이 True 이면 x 값이 사용되고&#44; True가 아니면 y 값이 사용되도록 하는 코드이다. <br />
<br />
예를 들어<br />
0 if 123&gt;456 else 1<br />
과 같은 표현식의 평가값은 123 &gt; 456 의 비교연산 결과가 False 이므로 1이 된다. <br />
<br />
예시 코드에서 <br />
a&gt;=b 의 결과가 True(참) 이면 (a if (a&gt;=b) else b)의 결과는 a가 되고&#44; <br />
<span>a&gt;=b 의 결과가&nbsp;</span>False(거짓)이면 (a if (a&gt;=b) else b)의 결과는 b가 된다.<br />
<br />

### 입력

두 정수가 공백을 두고 입력된다.<br />
-2147483648 ~ +2147483647 <br />
<br />

### 출력

두 정수 중 큰 값을 10진수로 출력한다. <br />
<br />

### 입력 예시

<pre>123 456</pre>

### 출력 예시

<pre>456</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
