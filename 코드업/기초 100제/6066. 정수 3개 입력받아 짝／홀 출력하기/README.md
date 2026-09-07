# [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py) - 6066

[문제 링크](https://codeup.kr/problem.php?id=6066)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-조건/선택실행구조

### 채점결과

정확한 풀이

### 문제 설명

<span>본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;</span><br />
<span>------</span><br />
<br />
3개의 정수(a&#44; b&#44; c)가 입력되었을 때&#44; 짝(even)/홀(odd)을 출력해보자. <br />
<br />
예시<br />
... <br />
if a%2==0 : <br />
&nbsp; print("even") <br />
else : <br />
&nbsp; print("odd")&nbsp; <br />
... <br />
<br />
참고&nbsp;<br />
if 조건식 :&nbsp; #조건식을 평가해서...<br />
&nbsp; 실행1&nbsp; &nbsp; &nbsp; #True 인 경우 실행시킬 명령들...<br />
&nbsp; 실행2 <br />
else :&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br />
&nbsp; 실행3&nbsp; &nbsp; &nbsp;&nbsp;<span>#False 인 경우 실행시킬 명령들...</span> <br />
&nbsp; 실행4 <br />
실행5&nbsp; &nbsp; &nbsp; &nbsp;#조건식과 상관없는 다음 명령<br />
... <br />
<br />

	else 는 if 없이 혼자 사용되지 않는다.
<br />

	또한&#44; else 다음에는 조건식이 없는 이유는? True(참)가 아니면 False(거짓)이기 때문에...&nbsp;
<br />
조건식의 평가 결과는 True 아니면 False 로 계산되기 때문이다. <br />
<br />
<span>python</span> 에서는 들여쓰기를 기준으로 코드블록을 구분하므로&#44; 들여쓰기를 정확하게 해주어야 한다. <br />
<br />

### 입력

3개의 정수(a&#44; b&#44; c)가 공백을 두고 입력된다.<br />
0 &lt;= a&#44;b&#44;c &lt;= 2147483647 <br />
<br />

### 출력

입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다. <br />
<br />

### 입력 예시

<pre>1 2 8</pre>

### 출력 예시

<pre>odd
even
even</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
