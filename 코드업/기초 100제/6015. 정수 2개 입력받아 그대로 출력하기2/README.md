# [기초-입출력] 정수 2개 입력받아 그대로 출력하기2(설명)(py) - 6015

[문제 링크](https://codeup.kr/problem.php?id=6015)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-입출력

### 채점결과

정확한 풀이

### 문제 설명

<p>본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.&nbsp;<br />
------<br />
<br />
공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.<br />
<br />
예시<br />
a, b = input().split()<br />
a=int(a)<br />
b=int(b)<br />
print(a)<br />
print(b)<br />
과 같은 방법으로 두 정수를 입력받아 출력할 수 있다.<br />
<br />
참고<br />
python의 input()은 한 줄 단위로 입력을 받는다.<br />
input().<span style="color:#e53333">split</span>() 를 사용하면, 공백을 기준으로 입력된 값들을 나누어(<span style="color:#e53333">split</span>) 자른다.<br />
a, b = 1, 2<br />
를 실행하면, a에는 1 b에는 2가 저장된다.<br />
(주의 : 하지만, 다른 일반적인 프로그래밍언어에서는 이러한 방법을 지원하지 않기 때문에 a=1, b=2 를 한 번에 하나씩 따로 실행시켜야 한다.)<br />
&nbsp;</p>

### 입력

<p>2개의 정수가 공백으로 구분되어 입력된다.<br />
&nbsp;</p>

### 출력

<p>입력된 두 정수를 줄을 바꿔 출력한다.<br />
&nbsp;</p>

### 입력 예시

<pre>1 2</pre>

### 출력 예시

<pre>1
2</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
