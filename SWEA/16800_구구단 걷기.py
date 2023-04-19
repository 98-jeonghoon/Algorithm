# t = int(input())
# for test in range(t):
#     n = int(input())
#     graph = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = (i + 1) * (j + 1)

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     def bfs(x, y):
#         from collections import deque
#         visited = [[False] * n for _ in range(n)]
#         dist = [[0] * n for _ in range(n)]
#         queue = deque()
#         queue.append((x, y))
#         visited[x][y] = True
        
#         while queue:
#             x, y = queue.popleft()
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if visited[nx][ny] == False:
#                         dist[nx][ny] = dist[x][y] + 1
#                         visited[nx][ny] = True
#                         queue.append((nx, ny))
#         return dist

#     dist = bfs(0, 0)

#     answer = 1e9
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == n:
#                 answer = min(answer, dist[i][j])
#     print('#{} {}'.format(test+1, answer))

# t = int(input())
# for test in range(t):
#     n = int(input())
#     graph = [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     def bfs(x, y):
#         from collections import deque
#         dist = [[0] * n for _ in range(n)]
#         queue = deque()
#         queue.append((x, y))
#         dist[x][y] = 1
        
#         while queue:
#             x, y = queue.popleft()
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if dist[nx][ny] == 0:
#                         dist[nx][ny] = dist[x][y] + 1
#                         queue.append((nx, ny))
#         return dist

#     dist = bfs(0, 0)

#     answer = 1e9
#     for i, row in enumerate(graph):
#         for j, val in enumerate(row):
#             if val == n:
#                 answer = min(answer, dist[i][j] - 1)
#     print('#{} {}'.format(test+1, answer))

import math

t = int(input())
for test in range(t):
    n = int(input())
    
    answer = float('inf')
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            answer = min(answer, i + j - 2)
    
    print('#{} {}'.format(test+1, answer))
