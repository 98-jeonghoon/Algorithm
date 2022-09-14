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

a = input()
list = list(a)
print(type(int(a[1])))