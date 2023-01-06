# 삼성 SW 코테 문제에 벽을 느끼고 푸는 문제들

## 백준 1260 DFS와 BFS

# n, m, v = map(int, input().split())
# graph = [[] * m for _ in range(n+1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(n+1):
#     graph[i].sort()


# visited = [False] * (n+1)

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# dfs(graph, v, visited)


# visited = [False] * (n+1)
# from collections import deque

# def bfs(graph, v, visited):
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         now = queue.popleft()
#         print(now, end=' ')
#         for i in graph[now]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# print()         
# bfs(graph, v, visited)

## 바이러스 백준 2606번
# n = int(input())
# m = int(input())
# graph = [[] * m for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# for i in range(n):
#     graph[i].sort()
# visited = [False] * (n+1)

# count = 0
# def dfs(graph, v, visited):
#     global count
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             count += 1
#             dfs(graph, i, visited)

# dfs(graph, 1, visited)
# print(count)

## 단지번호붙이기 백준 2667번

# n = int(input())
# graph = [list(map(int, input())) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# count = 0
# def dfs(x,y):
#     global count
#     if x < 0 or y < 0 or x >= n or y >= n:
#         return
#     if graph[x][y] == 0:
#         return
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         count += 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)
#     return count

# arr = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             arr.append(dfs(i,j))
#             count = 0

# arr.sort()
# print(len(arr))
# for i in arr:
#     print(i)

## 유기농 배추 백준 1012
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def dfs(x, y):
#     global count
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return
#     if graph[x][y] == 0:
#         return
#     if graph[x][y] == 1:
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)

# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#     for i in range(k):
#         a, b = map(int, input().split())
#         graph[b][a] = 1
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 dfs(i, j)
#     print(count)

## 적록색약 백준 10026

n = int(input())
graph = [list(input()) for _ in range(n)]

