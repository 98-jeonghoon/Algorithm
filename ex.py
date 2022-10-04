# n, m = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1 , y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# count = 0 

# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             count += 1
            
# print(count)

# from collections import deque
            
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >=m:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
                
#     return graph[n - 1][m - 1]

# print(bfs(0, 0))


# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int ,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# for i in range(n+1):
#     graph[i].sort()
    
# visited = [False] * (n + 1)

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
        
# dfs(graph, v, visited)
# print()
  
# from collections import deque

# visited = [False] * (n + 1)

# def bfs(graph, v, visited):
#     queue = deque()
#     queue.append(v)
#     visited[v] = True
#     while queue:
#         now = queue.popleft()
#         print(now, end=' ')
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
                
# bfs(graph, v, visited)

# from collections import deque

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
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
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
                
#     return graph[n -1][m -1]

# print(bfs(0, 0))

# from collections import deque

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# for i in range(n+1):
#     graph[i].sort()
    
# visited = [False] * (n + 1)
# count = 0

# def bfs(graph, v, visited):
#     global count
#     queue = deque()
#     queue.append(v)
#     visited[v] = True
#     while queue:
#         now = queue.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#                 count += 1
# # def dfs(graph, v, visited):
# #     global count
# #     visited[v] = True
# #     for i in graph[v]:
# #         if not visited[i]:
# #             dfs(graph, i, visited)
# #             count += 1
            
# # dfs(graph, 1, visited)
# bfs(graph, 1, visited)
# print(count)

# from collections import deque

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1 ,1]
# apt = []
# def bfs(x,y):
#     graph[x][y] = 0
#     count = 1
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
#                 count += 1
#     apt.append(count)
    
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             bfs(i,j)
            
# print(len(apt))
# apt.sort()
# for i in range(len(apt)):
#     print(apt[i])



# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     graph[x][y] = 0
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
                

# t = int(input())
# for _ in range(t):
#     count = 0
#     m, n, k = map(int, input().split())
#     graph = [[0]*m for _ in range(n)]

#     for _ in range(k):
#         a, b = map(int ,input().split())
#         graph[b][a] = 1
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 bfs(i,j)
#                 count += 1
#     print(count)

# from collections import deque

# m, n = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs():
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
                
# queue = deque()
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             queue.append((i,j))

# bfs()

# days = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             print(-1)
#             exit(0)
#         days = max(days, graph[i][j])
    
# print(days-1)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()
    
print(graph)