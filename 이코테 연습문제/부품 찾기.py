# 이진 탐색을 이용한 풀이
n = int(input())
array = list(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start +  end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in guest:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수 정렬을 이용한 풀이
# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1
    
# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


# 집합 자료형을 이용한 풀이
# n = int(input())
# array = set(map(int, input().split()))
# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i in array:
#         print('yse', end=' ')
#     else:
#         print('no', end=' ')
        