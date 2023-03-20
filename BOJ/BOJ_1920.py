n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
target = list(map(int, input().split()))
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for num in target:
    result = binary_search(arr, num, 0, n - 1)
    if result == True:
        print(1)
    else:
        print(0)
            