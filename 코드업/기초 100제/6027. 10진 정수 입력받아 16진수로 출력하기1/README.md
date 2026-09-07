# [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1(설명)(py) - 6027

[문제 링크](https://codeup.kr/problem.php?id=6027)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-출력변환

### 채점결과

정확한 풀이

### 문제 설명

<span>본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;</span><br />
<span>------</span><br />
<br />
10진수를 입력받아 16진수(hexadecimal)로 출력해보자. <br />
<br />
예시 <br />
a = input() <br />
n = int(a)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #입력된 a를 10진수 값으로 변환해 변수 n에 저장 <br />
print('%<span style="color:#E53333;">x</span>'% n)&nbsp; #n에 저장되어있는 값을 16진수(he<span style="color:#E53333;">x</span>adecimal) <span style="color:#E53333;">소문자</span> 형태 문자열로 출력<br />
<br />
참고<br />
10진수 형태로 입력받고<br />
%x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.<br />
(%o로 출력하면 8진수(octal) 문자열로 출력된다.)<br />
<br />
10진법은 한 자리에 10개(0 1 2 3 4 5 6 7 8 9)의 문자를 사용하고&#44;<br />
16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 a b c d e f)의 문자를 사용한다.<br />
16진수 a는 10진수의 10&#44; b는 11&#44; c는 12 ... 와 같다.<br />
<p style="text-align:right;">
	<img src="/admin/../upload/pimg6192_1.png" alt="" /> <br />
<br />
<br />

### 입력

10진수 1개가 입력된다.<br />
<br />

### 출력

16진수(소문자) 형태로 출력한다.<br />
<br />

### 입력 예시

<pre>255</pre>

### 출력 예시

<pre>ff</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
