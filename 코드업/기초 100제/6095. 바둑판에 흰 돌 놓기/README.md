# [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py) - 6095

[문제 링크](https://codeup.kr/problem.php?id=6095)

### 성능 요약

시간 제한: 1 Sec, 메모리 제한: 128 MB

### 구분

코드업 > 기초 100제

### 문제 분류

기초-리스트

### 채점결과

정확한 풀이

### 문제 설명

<span>본 문제는 <span>python</span> 의 빠른 기초 학습을 위해 설계된 문제로서 <span>python</span> 코드 제출을 기준으로 설명되어 있습니다.&nbsp;</span><br />
<span>------</span><br />
<br />
기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 모두 집으로 귀가를 한다. <br />
<br />
오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가<br />
"바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.<br />
<br />
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때&#44;<br />
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.<br />
<br />
예시 <br />
d=[]&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기 <br />
for i in range(20) : <br />
&nbsp; d.append([])&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;#리스트 안에 다른 리스트 추가해 넣기 <br />
&nbsp; for j in range(20) :&nbsp; <br />
&nbsp; &nbsp; d[i].append(0)&nbsp; &nbsp; #리스트 안에 들어있는 리스트 안에 0 추가해 넣기 <br />
<br />
n = int(input()) <br />
for i in range(n) : <br />
&nbsp; x&#44; y = input().split() <br />
&nbsp; d[int(x)][int(y)] = 1 <br />
<br />
for i in range(1&#44; 20) : <br />
&nbsp; for j in range(1&#44; 20) :&nbsp; <br />
&nbsp; &nbsp; print(d[i][j]&#44; end=' ')&nbsp; &nbsp; #공백을 두고 한 줄로 출력 <br />
&nbsp; print()&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #줄 바꿈 <br />
<br />
참고<br />
리스트가 들어있는 리스트를 만들면? <br />
가로번호&#44; 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.<br />
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있고&#44; 더 확장한 n차원의 리스트도 만들 수 있다. <br />
<br />
... <br />
<span>d=[]</span><br />
<span>for i in range(20) :&nbsp;</span><br />
<span>&nbsp; d.append([])</span><br />
<span>&nbsp; for j in range(20) :&nbsp;&nbsp;</span><br />
<span>&nbsp; &nbsp; d[i].append(0)</span><br />
...&nbsp; <br />
<br />
위와 같이&#44; 모두 0이 채워진 2차원 리스트를 만드는 코드를 아래와 같은 방법으로 짧게 만들 수도 있다. <br />
... [0 for j in range(20)]&nbsp; #20개의 0이 들어간 [0&#44; 0&#44; 0&#44; ... &#44; 0&#44; 0&#44; 0] 리스트&nbsp;<br />
아래처럼 작성하면 위와 같은 리스트가 20개가 들어간 리스트를 한 번에 만들어 준다. <br />
<br />
d = [[0 for j in range(20)] for i in range(20)] <br />
<br />
이러한 리스트 생성 방식을 List Comprehensions 라고 한다. <br />
<p style="text-align:right;">
	<img src="/admin/../upload/pimg6260_1.png" alt="" /> <br />
<br />
<br />

### 입력

바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.<br />
둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x&#44; y)가 n줄 입력된다.<br />
n은 10이하의 자연수이고 x&#44; y 좌표는 1 ~ 19 까지이며&#44; 똑같은 좌표는 입력되지 않는다. <br />
<br />

### 출력

흰 돌이 올려진 바둑판의 상황을 출력한다.<br />
흰 돌이 있는 위치는 1&#44; 없는 곳은 0으로 출력한다. <br />
<br />

### 입력 예시

<pre>5
1 1
2 2
3 3
4 4
5 5</pre>

### 출력 예시

<pre>1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0</pre>

> 출처: [코드업 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
