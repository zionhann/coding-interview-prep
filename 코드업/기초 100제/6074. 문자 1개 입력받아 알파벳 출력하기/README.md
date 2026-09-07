# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py) - 6074

[문제 링크](https://codeup.kr/problem.php?id=6074)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-반복실행구조

### 채점결과

정확한 풀이

### 문제 설명

<span>본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;</span><br />
<span>------</span><br />
<br />
영문 소문자(a ~ z) 1개가 입력되었을 때&#44; <br />
a부터 그 문자까지의 알파벳을 순서대로 출력해보자. <br />
<br />
예시 <br />
c = ord(input()) <br />
t = ord('a') <br />
while t&lt;=c : <br />
&nbsp; print(chr(t)&#44; end=' ') <br />
&nbsp; t += 1 <br />
<br />
참고 <br />
알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다. <br />
chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다. <br />
print(...&#44; end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력한다. 즉&#44; 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.<br />
(end='\n'로 작성하거나 생략하면&#44; 값을 출력한 후 마지막(end)에 줄바꿈(newline)이 된다.) <br />
<br />

### 입력

영문자 1개가 입력된다.<br />
(a ~ z) <br />
<br />

### 출력

a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다. <br />
<br />

### 입력 예시

<pre>f</pre>

### 출력 예시

<pre>a b c d e f</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
