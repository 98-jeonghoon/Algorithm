n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()

start = 1
end = max(arr)
answer = 0
while start <= end:
    mid = (start + end) // 2
    
    total = 0

    for i in arr:
        if i <= mid:
            total += i
        else:
            total += mid
    
    if total <= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
