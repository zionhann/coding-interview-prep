# [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py) - 6067

[문제 링크](https://codeup.kr/problem.php?id=6067)

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
0이 아닌 정수 1개가 입력되었을 때&#44; 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자. <br />
음수이면서 짝수이면&#44; A<br />
음수이면서 홀수이면&#44; B<br />
양수이면서 짝수이면&#44; C<br />
양수이면서 홀수이면&#44; D<br />
를 출력한다.<br />
<br />
예시 <br />
... <br />
if n&lt;0 : <br />
&nbsp; if n%2==0 : <br />
&nbsp; &nbsp; print('A')&nbsp; &nbsp; &nbsp; #주의 : 변수 A와 문자열 'A' / "A" 는 의미가 완전히 다르다.&nbsp;<br />
&nbsp; else : <br />
&nbsp; &nbsp; print('B') <br />
else : <br />
&nbsp; if n%2==0 : <br />
&nbsp; &nbsp; print('C') <br />
&nbsp; else : <br />
&nbsp; &nbsp; print('D') <br />
... <br />
<br />
참고 <br />
조건/선택 실행구조 안에 다시 조건/선택 실행구조를 "중첩"할 수가 있다. <br />
<br />
또한&#44; 중첩된 조건은<br />

	...
<br />

	if (n&lt;0) and (n%2==0) :
<br />

	&nbsp; &nbsp; print('A')
<br />
<div>
	...

### 입력

정수 1개가 입력된다.<br />
-2147483648 ~ +2147483647&#44; 단 0은 입력되지 않는다. <br />
<br />

### 출력

음수이면서 짝수이면&#44; A<br />
음수이면서 홀수이면&#44; B<br />
양수이면서 짝수이면&#44; C<br />
양수이면서 홀수이면&#44; D<br />
를 출력한다.<br />
<br />

### 입력 예시

<pre>-2147483648</pre>

### 출력 예시

<pre>A</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
