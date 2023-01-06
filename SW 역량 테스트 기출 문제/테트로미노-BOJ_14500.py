n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 하늘색
blue = [0, 0, 0, 0]

from collections import deque

arr = [[1,0],
       [1,0],
       [1,1]]

arr = deque(arr)
arr.rotate(2)
print(arr)