h, w = map(int, input().split())
block = list(map(int, input().split()))

answer = 0
for i in range(1, w - 1):
    left = max(block[:i])
    right = max(block[i + 1:])

    lower_one = min(left, right)

    if block[i] < lower_one:
        answer += lower_one - block[i]

print(answer)