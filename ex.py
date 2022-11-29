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

# from collections import deque

# n, m = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# for i in range(n+1):
#     graph[i].sort()
    
# visited = [False] * (n+1)

# def bfs(graph, v, visited):
#     queue = deque()
#     queue.append(v)
#     visited[v] = True
#     while queue:
#         now = queue.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
                
# count = 0
# for i in range(1, n+1):
#     if not visited[i]:
#         bfs(graph, i, visited)
#         count += 1
# print(count)

# from collections import deque
# import copy

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs():
#     global answer
#     queue = deque()
#     tmp_graph = copy.deepcopy(graph)
#     for i in range(n):
#         for j in range(m):
#             if tmp_graph[i][j] == 2:
#                 queue.append((i, j))
                
#     while queue:
#         x, y =queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if tmp_graph[nx][ny] == 1:
#                 continue
#             if tmp_graph[nx][ny] == 0:
#                 tmp_graph[nx][ny] = 2
#                 queue.append((nx, ny))
                
#     cnt = 0
    
#     for i in range(n):
#         cnt += tmp_graph[i].count(0)
    
#     answer = max(answer, cnt)

# def make_wall(cnt):
#     if cnt == 3:
#         bfs()
#         return
        
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 make_wall(cnt+1)
#                 graph[i][j] = 0
                
# answer = 0
# make_wall(0)
# print(answer)


# from collections import deque

# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     graph[x][y] = 0
#     while queue:
#         x, y = queue.popleft()
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= h or ny >= w:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
                
# while True:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
#     graph = []
#     count = 0
#     for _ in range(h):
#         graph.append(list(map(int, input().split())))
        
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1:
#                 bfs(i, j)
#                 count += 1
#     print(count)


# from collections import deque
# import copy

# n, m = map(int, input().split())
# graph = []
# for _  in range(n):
#     graph.append(list(map(int, input().split())))
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# answer = 0
# def bfs():
#   count = 0
#   global answer
#   queue = deque()
#   tmp_graph = copy.deepcopy(graph)
#   for i in range(n):
#     for j in range(m):
#       if tmp_graph[i][j] == 2:
#         queue.append((i, j))

#   while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if nx < 0 or ny < 0 or nx >= n or ny >=m:
#         continue
#       if tmp_graph[nx][ny] == 0:
#         tmp_graph[nx][ny] = 2
#         queue.append((nx, ny))

#   for i in range(n):
#     count += tmp_graph[i].count(0)
#     answer = max(answer, count)
#   return answer
  
# def wall(cnt):
#   if cnt == 3:
#     bfs()
#     return

#   for i in range(n):
#     for j in range(m):
#       if graph[i][j] == 0:
#         graph[i][j] = 1
#         wall(cnt+1)
#         graph[i][j] = 0
# wall(0)
# print(bfs())


# def solution(brown, yellow):
#     total = yellow + brown
#     for b in range(1, total+1):
#         if (total / b) % 1 == 0:
#             a = total // b
#             if a >= b:
#                 if 2*a + 2*b == brown + 4:
#                     return [a, b]
                

# print(solution(10 ,2))


arr = list(map(int, input().split()))
total = sum(arr)
print(total)