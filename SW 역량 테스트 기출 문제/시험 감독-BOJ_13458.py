n = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

answer = n
for i in arr:
    i -= B
    if i > 0:
        if i % C:
            answer += (i // C) + 1
        else:
            answer += (i // C)

print(answer)