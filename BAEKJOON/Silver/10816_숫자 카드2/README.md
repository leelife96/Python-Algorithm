    
### [문제링크](https://www.acmicpc.net/problem/10816)

### <span style="color:orange"> 문제 해석 </span>
이 문제는 list의 count함수를 사용하면 문제가 풀리긴 하지만 시간초과가 발생한다.
collections 패키지의 Counter 함수를 사용하면 시간초과 없이 문제를 해결할 수 있다.

### 

### <span style="color:orange"> [풀이 과정] </span>
1. input을 쓰면 시간초과가 나오니, 꼭 readline을 쓰자
2. count() 대신 Counter() 사용하기 -> Counter은 빈도수를 딕셔너리 형태로 만듬