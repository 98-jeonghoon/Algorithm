## 1트 실패
# import copy
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
# dx = [0, -1, -1, -1, 0, 1, 1, 1]
# dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# check_move = [1, 3, 5, 7]
# cloud = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]

# cmd = []
# for _ in range(m):
#     d, s = map(int, input().split())
#     cmd.append((d - 1, s))

# for _ in range(m):
#     d, s = cmd.pop(0)
#     tmp_visited = copy.deepcopy(visited)
#     while cloud:
#         x, y = cloud.pop(0)
#         nx = (x + s * dx[d]) % n
#         ny = (y + s * dy[d]) % n
#         graph[nx][ny] += 1
#         count = 0
#         for i in check_move:
#             check_nx = nx + dx[i]
#             check_ny = ny + dy[i]
#             if check_nx < 0 or check_ny < 0 or check_nx >= n or check_ny >= n:
#                 continue
#             if graph[check_nx][check_ny] == 0:
#                 continue
#             count += 1
#         graph[nx][ny] += count
#         tmp_visited[nx][ny] = True

#     for i in range(n):
#         for j in range(n):
#             if tmp_visited[i][j] ==False and graph[i][j] >= 2:
#                 graph[i][j] -= 2
#                 cloud.append((i, j))
        
        
# for i in graph:
#     print(i)

# 2트

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
check_move = [1, 3, 5, 7]
cloud = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]

cmd = []
for _ in range(m):
    d, s = map(int, input().split())
    cmd.append((d - 1, s))


for _ in range(m):
    d, s = cmd.pop(0)
    new_cloud = []
    visited = [[False] * n for _ in range(n)]
    for _ in range(len(cloud)):
        x, y = cloud.pop(0)
        nx = (x + s * dx[d]) % n
        ny = (y + s * dy[d]) % n
        new_cloud.append((nx, ny))
        
    for i in range(len(new_cloud)):
        x, y = new_cloud[i]
        graph[x][y] += 1
        visited[x][y] = True
        

    
    for i in range(len(new_cloud)):
        x, y = new_cloud[i]
        count = 0
        for i in check_move:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] >= 1:
                count += 1
        graph[x][y] += count

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and graph[i][j] >= 2:
                graph[i][j] -= 2
                cloud.append((i, j))
        
answer = 0   
for i in graph:
    answer += sum(i)
print(answer)