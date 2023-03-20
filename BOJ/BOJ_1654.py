k, n = map(int, input().split())
lans = []
for _ in range(k):
    lan = int(input())
    lans.append(lan)

start = 0
end = max(lans)

while start <= end:
    mid = (start + end) // 2

    total = 0

    for i in range(k):
        total += lans[i] // mid
    
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)