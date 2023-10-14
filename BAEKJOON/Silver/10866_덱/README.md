    
### [문제링크](https://www.acmicpc.net/problem/10866)

### <span style="color:orange"> 문제 해석 </span>
문제에서 주어진 명령어를 모두 구현하면 되는 문제이다. 대부분 명령어들이 deque에서 지원하는 명령어와 같다.
append, appendLeft, pop, popLeft를 사용하여 쉽게 해결 할 수 있는 문제이다.


### 

### <span style="color:orange"> [풀이 과정] </span>
1. input을 쓰면 시간초과가 나오니, 꼭 readline을 쓰자
2. from collections import deque 모듈을 선언해준다
3. 모듈을 써서 popleft() 등을 사용하여 빼내고 출력을 하였다.