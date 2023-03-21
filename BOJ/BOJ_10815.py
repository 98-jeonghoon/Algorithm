n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

cards.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if target == arr[mid]:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return False

for i in find:
    result = binary_search(cards, i, 0, n - 1)
    if result:
        print(1, end=' ')
    else:
        print(0, end=' ')