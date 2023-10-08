import sys

N = int(sys.stdin.readline())
word = []
for _ in range(N):
    word.append(sys.stdin.readline().strip())

word = list(set(word)) ## word의 중복된 요소를 제거하고 리스트로 다시 만듬
word.sort() ## 사전 순서대로 정렬함
word.sort(key=len) ## key=len을 주어서 짧은 길이 순으로 다시 정렬

for i in word:
    print(i)