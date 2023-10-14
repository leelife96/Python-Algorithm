    
### [문제링크](https://www.acmicpc.net/problem/2798)

### <span style="color:orange"> 문제 해석 </span>
이 문제는 모든 경우의 수를 다 뒤져봐야 하는 완전 탐색 문제이다.

### 

### <span style="color:orange"> [풀이 과정] </span>
1. N, M을 입력받아 int로 변환한다
2. 카드에 쓰여져 있는 수들을 list화 시켜 저장한다
3. 문제의 결과 값을 반환하기 위해 result 선언
4. 3개의 카드를 뽑아야 하므로 이에 대한 모든 경우의 수를 보기위해 3중 for문 사용
5. 세 카드의 값이 M 보다 클 경우 continue, M 보다 크지 않을 경우 일단의 정답에 가능성이 있으니 result에 저장한다
6. 