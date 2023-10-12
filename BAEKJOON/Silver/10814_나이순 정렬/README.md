
### [문제링크](https://www.acmicpc.net/problem/10814)

### <span style="color:orange"> 문제 해석 </span>
sort() 함수와 lambda 식을 써서 답을 구하는 문제이다. 
나이와 이름은 자료형 타입이 각각 다르니까 입력을 넣어 준 후에 타입을 바꿔주는게 포인트다.

### [람다식 정렬 링크](https://soopeach.tistory.com/23)

### <span style="color:orange"> [풀이 과정] </span>
1. X, Y = sys.stdin.readline().split() 를 써서 X와 Y에 각각 입력을 대입
2. X는 나이이니 int형으로 변환해준다
3. lamdba를 써서 x[0]에 있는 나이순으로 오름차순 정렬 해준다