# import copy
# from collections import deque

# n, m = map(int, input().split())
# graph = [list(input()) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y, graph):
#     tmp_graph = copy.deepcopy(graph)
#     visitied = [[False] * m for _ in range(n)]
#     dist = [[-1] * m for _ in range(n)]
#     visitied[x][y] = True
#     dist[x][y] = 1
#     queue = deque()
#     queue.append((x, y))
    
#     while queue:
#         x, y = queue.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if visitied[nx][ny] == False and tmp_graph[nx][ny] == '0':
#                     dist[nx][ny] = dist[x][y] + 1
#                     visitied[nx][ny] = True
#                     queue.append((nx, ny))
#     return dist[n - 1][m - 1]

# answer = -1e9
# def back_tracking(depth):
#     global answer
#     if depth == 1:
#         answer = max(bfs(0, 0, graph), answer)
#         return
#     for x in range(n):
#         for y in range(m):
#             if graph[x][y] == '1':
#                 graph[x][y] = '0'
#                 back_tracking(depth + 1)
#                 graph[x][y] = '1'

# back_tracking(0)
# print(answer)

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(visited)
def solve(x, y, wall_break_left, visited, graph):
    queue = deque()
    queue.append((x, y, wall_break_left))
    visited[x][y][wall_break_left] = 1

    while queue:
        x, y, wall_break_left = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall_break_left]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
                queue.append((nx, ny, wall_break_left))
                visited[nx][ny][wall_break_left] = visited[x][y][wall_break_left] + 1
            if graph[nx][ny] == 1 and wall_break_left == 1:
                queue.append((nx, ny, wall_break_left - 1))
                visited[nx][ny][wall_break_left - 1] = visited[x][y][wall_break_left] + 1

    return -1

print(solve(0, 0, 1, visited, graph))