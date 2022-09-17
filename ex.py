# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))


# def dfs(x,y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)
#         return True
#     return False

                
# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     count = 0
#     graph = [[0]*m for _ in range(n)]

#     for _ in range(k):
#         a, b = map(int , input().split())
#         graph[b][a] = 1
    
#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j) == True:
#                 count += 1
#     print(count)

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid -1
#         else:
#             start = mid + 1
#     return None

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print('원소 존재 하지 않음')
# else:
#     print(result + 1)


# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print('원소 존재 X')
# else:
#     print(result+1)

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1) + fibo(x-2)

# print(fibo(50))

d = [0] * 1000

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(99))

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])