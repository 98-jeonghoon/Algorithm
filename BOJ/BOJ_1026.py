# 길이가 N인 정수 배열 A, B
# 함수 S = a[0] x b[0] + .... + a[n-1] + b[n-1]
# S값이 최솟값이 되도록 A 정렬하고 최솟값 출력하기

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

max_value = 0
for i in range(n):
    max_value += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
    
print(max_value)