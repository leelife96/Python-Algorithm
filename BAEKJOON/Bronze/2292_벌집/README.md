    
### [문제링크](https://www.acmicpc.net/problem/2292)

### <span style="color:orange"> 문제 해석 </span>
이 문제는 랜덤으로 숫자 N이 주어질 때 1이 있는 벌집 위치에서 숫자 N까지 거쳐가는 단계의 수를 찾아내는 문제이다.
다시 말해서 숫자 N이 벌집에서 몇 겹째에 있는지를 출력하는 문제이다.

### 

### <span style="color:orange"> [풀이 과정] </span>
1. 0이 입력되면 pop() 함수로 리스트의 마지막 원소를 리턴하고 삭제한다
2. 0이 아닌 숫자가 오면 append() 함수로 리스트에 넣는다
3. 그리고 sum 함수로 합계를 계산한다