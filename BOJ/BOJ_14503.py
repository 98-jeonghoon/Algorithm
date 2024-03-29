# n, m = map(int, input().split())
# r, c, d = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# visited = [[0] * m for _ in range(n)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# visited[r][c] = 1
# count = 1

# while True:
#     flag = 0
#     for _ in range(4):
#         d = (d+3) % 4
#         nx = r + dx[d]
#         ny = c + dy[d]
#         if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 count += 1
#                 r = nx
#                 c = ny
#                 flag = 1
#                 break
#     if flag == 0:
#         if graph[r-dx[d]][c-dy[d]] == 1:
#             print(count)
#             break
#         else:
#             r, c = r-dx[d], c-dy[d]


n, m = map(int, input().split())
r, c , d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
graph[r][c] = 2
while True:
    flag = 0
    for i in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            count += 1
            r, c = nx, ny
            flag = 1
            break
    
    if flag == 0:
        if graph[r - dx[d]][c - dy[d]] == 1:
            print(count)
            break
        else:
            r, c = r - dx[d], c - dy[d]