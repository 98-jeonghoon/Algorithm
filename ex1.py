# from collections import deque

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >=m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# T = int(input())
# for _ in range(T):
#     m , n, k = map(int, input().split())
#     graph = [[0]*m for _ in range(n)]
#     count = 0
#     for i in range(k):
#         a, b= map(int, input().split())
#         graph[b][a] = 1
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 bfs(i,j)
#                 count +=1    
#     print(count)

from collections import deque
n , m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

count = 0

for i in range(1, n+1):
  if not visited[i]:
    bfs(graph, i, visited)
    count += 1

print(count)