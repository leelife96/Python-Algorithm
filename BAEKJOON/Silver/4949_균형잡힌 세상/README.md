
### [문제링크](https://www.acmicpc.net/problem/4949)

### <span style="color:orange"> 문제 해석 </span>
스택에 append로 쌓아 놓고 문제의 조건에 맞으면 pop를 써서 빼주는 문제이다.

### <span style="color:orange"> [풀이 과정] </span>
1. . 이 들어오면 break로 반복문 탈출
2. 반복문을 돌면서 i가 '(' or '[' 라면 stack.append 로 스택에 추가하기
3. i가 )일때 스택의 길이가 0이 아니라면 그리고 스택의 맨 위에 문자가 '('라면 stack.pop으로 스택에서 빼기
4. 아니라면 'no', break
5. i가 ] 일때 스택의 길이가 0이 아니라면 그리고 스택의 맨 위에 문자가 [ 라면 stack.pop 으로 스택에서 빼기
6. 아니라면 no, break
7. stack의 길이가 0이라면 'yes'출력
8. 아니라면 'no' 출력
