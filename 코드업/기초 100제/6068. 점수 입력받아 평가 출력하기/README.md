# [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py) - 6068

[문제 링크](https://codeup.kr/problem.php?id=6068)

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
점수(정수&#44; 0 ~ 100)를 입력받아 평가를 출력해보자. <br />
<br />
평가 기준<br />
점수 범위 : 평가<br />
&nbsp;90 ~ 100 : A<br />
&nbsp;70 ~ &nbsp; 89 : B<br />
&nbsp;40 ~ &nbsp; 69 : C<br />
&nbsp;&nbsp;&nbsp;0 ~ &nbsp; 39 : D<br />
로 평가되어야 한다.<br />
<br />
예시 <br />
... <br />
if n&gt;=90 : <br />
&nbsp; print('A') <br />
else : <br />
&nbsp; if n&gt;=70 : <br />
&nbsp; &nbsp; print('B') <br />
&nbsp; else : <br />
&nbsp; &nbsp; if n&gt;=40 : <br />
&nbsp; &nbsp; &nbsp; print('C') <br />
&nbsp; &nbsp; else : <br />
&nbsp; &nbsp; &nbsp; print('D')&nbsp; <br />
... <br />
<br />
참고 <br />
여러 조건들을 순서대로 비교하면서 처리하기 위해서 조건문을 여러 번 중첩할 수 있다.<br />
<br />
if 조건식1 : <br />
&nbsp; ... <br />
else : <br />
&nbsp; if 조건식2 : <br />
&nbsp; &nbsp; ... <br />
&nbsp; else : <br />
&nbsp; &nbsp; if 조건식3 : <br />
&nbsp; &nbsp; &nbsp; ... <br />
&nbsp; &nbsp; else : <br />
<div>
	&nbsp; &nbsp; &nbsp; ...

### 입력

정수(0 ~ 100) 1개가 입력된다. <br />
<br />

### 출력

평가 결과를 출력한다. <br />
<br />

### 입력 예시

<pre>73</pre>

### 출력 예시

<pre>B</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
