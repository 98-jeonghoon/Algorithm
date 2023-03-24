n, c = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
arr.sort()

start = 1
end = arr[-1] - arr[0]
answer = 0
def binary_search(arr, start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]
        
        if count >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
            
binary_search(arr, start, end)
print(answer)