#### 파이썬 알고리즘 테스트

### [문제링크](https://www.acmicpc.net/problem/1436)

### <span style="color:orange"> 문제 해석 </span>
입력값에 넣은 문자열들을 길이가 짧은 순대로, 길이가 같으면 사전순으로 정렬을 한다.
단, 중복된 단어는 제거해야 함. sort와 sorted의 개념을 잘 알아두면 좋다

### [sort & sorted 개념] (https://cholink.tistory.com/142)

### <span style="color:orange"> [풀이 과정] </span>

1. input()을 쓰면 너무 느리기 때문에 readline()으로 입력해주는 것이 좋다.
2. word에 리스트를 생성해주고 word에 입력값들을 리스트 안에 넣어준다.
3. 그다음에는 중복된 요소를 제거해야 하니 set 함수를 써서 다시 list로 중복제거된 리스트로 만들어준다
4. word.sort()를 하면 문자열 즉, 사전 순서대로 정렬이 되고 
5. 우리는 짧은 길이 순서대로 정렬해야하니 word.sort(key=len)을 써서 정렬해주었다.


