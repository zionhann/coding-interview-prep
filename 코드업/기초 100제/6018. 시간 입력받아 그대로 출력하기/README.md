# [기초-입출력] 시간 입력받아 그대로 출력하기(설명)(py) - 6018

[문제 링크](https://codeup.kr/problem.php?id=6018)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-입출력

### 채점결과

정확한 풀이

### 문제 설명

<span>본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;</span><br />
<span>------</span><br />
<br />
24시간 시:분 형식으로 시간이 입력될 때&#44; 그대로 출력하는 연습을 해보자. <br />
<br />
예시<br />
a&#44; b = input().split(':')<br />
print(a&#44; b&#44; sep=':')<br />
와 같은 방법으로 가능하다.<br />
<br />
참고<br />
input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.<br />
print(?&#44; ?&#44; <span style="color:#E53333;">sep</span>=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.<br />
sep 는 분류기호(<span style="color:#E53333;">sep</span>erator)를 의미한다.<br />
&nbsp;<br />

### 입력

시(hour) 분(minute)이 콜론(':')으로 구분되어 한 줄로 입력된다. <br />
<br />

### 출력

입력받은 시간 형식과 똑같이 "시:분" 형태로 출력한다. <br />
<br />

### 입력 예시

<pre>3:16</pre>

### 출력 예시

<pre>3:16</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
