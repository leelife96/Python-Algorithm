
### [문제링크](https://www.acmicpc.net/problem/9012)

### <span style="color:orange"> 문제 해석 </span>
스택에 append로 쌓아 놓고 문제의 조건에 맞으면 pop를 써서 빼주는 문제이다.

### <span style="color:orange"> [풀이 과정] </span>
1. 스택 리스트를 만든다
2. '('가 들어오면 append로 스택에 넣어주고 ')'가 들어오면 스택의 길이가 0이고 스택의 마지막 요소가 ')'이면 pop으로 밀어준다
3. 스택의 길이가 0도 아니고 스택의 마지막 요소가 ')'도 아니면 append로 추가
4. stack의 길이가 0이라면 'yes'출력
5. 아니라면 'no' 출력
