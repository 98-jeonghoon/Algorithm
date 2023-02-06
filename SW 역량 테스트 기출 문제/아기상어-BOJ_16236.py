# from collections import deque

# INF = 1e9
# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# now_size = 2
# now_x, now_y = 0, 0

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
#     queue.append((now_x, now_y))
#     dist[now_x][now_y] = 0
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx and nx < n and 0 <= ny and ny < n:
#                 if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
#                     dist[nx][ny] = dist[x][y] + 1
#                     queue.append((nx, ny))

#     return dist

# def find(dist):
#     x, y = 0, 0
#     min_dist = INF
#     for i in range(n):
#         for j in range(n):
#             if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < now_size:
#                 if dist[i][j] < min_dist:
#                     x, y = i, j
#                     min_dist =dist[i][j]
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
#         result += value[2]
#         graph[now_x][now_y] = 0
#         ate += 1
#         if ate >= now_size:
#             now_size += 1
#             ate = 0
            
            
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            x, y = i, j

shark_size = 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def bfs(x, y):
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited

def find(visited):
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < shark_size:
                if visited[i][j] < min_dist:
                    x, y = i, j
                    min_dist = visited[i][j]
    if min_dist == 1e9:
        return None
    else:
        return x, y, min_dist
    
result = 0
ate = 0

while True:
    value = find(bfs(x, y))
    if value == None:
        print(result)
        exit(0)
    else:
        x, y = value[0], value[1]
        result += value[2]
        graph[x][y] = 0
        ate += 1
        if ate >= shark_size:
            shark_size += 1
            ate = 0