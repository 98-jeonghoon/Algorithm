# # 아기상어
# from collections import deque
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# now_x, now_y = 0, 0
# now_size = 2
# INF = 1e9

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 9:
#             graph[i][j] = 0
#             now_x, now_y = i, j

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs():
#     dist = [[-1] * n for _ in range(n)]
#     queue = deque()
#     dist[now_x][now_y] = 0
#     queue.append((now_x, now_y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
#                     dist[nx][ny] = dist[x][y] + 1
#                     queue.append((nx, ny))
#     return dist

# def find(dist):
#     x, y = 0, 0
#     min_dist = INF
#     for i in range(n):
#         for j in range(n):
#             if dist[i][j] != -1 and graph[i][j] >= 1 and graph[i][j] < now_size:
#                 if dist[i][j] < min_dist:
#                     min_dist = dist[i][j]
#                     x, y = i, j
#     if min_dist == INF:
#         return None
#     else:
#         return x, y, min_dist

# result = 0
# ate = 0

# while True:
#     value = find(bfs())
#     if value == None:
#         print(result)
#         exit(0)
#     else:
#         now_x, now_y = value[0], value[1]
#         result += value[-1]
#         graph[now_x][now_y] = 0
#         ate += 1
#         if ate >= now_size:
#             now_size += 1
#             ate = 0

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# dp = [0 for _ in range(n+1)]

# for i in range(n-1, -1, -1):
#     if i + arr[i][0] > n:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], arr[i][1] + dp[i + arr[i][0]])

# print(dp[0])
