n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))
print(arr)
last_end = 0
cnt = 0

for start, end in arr:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)