# # 시계방향으로 회전하는 코드 list(map(list, zip(*arr[::-1])))
# # 시계 반대방향으로 회전하는 코드 list(map(list, zip(*arr)))[::-1]
# # 1트 실패 -> 조건 1번에 같은 블록 그룹이 여러개일때를 처리 해주지 못해서 막혔음.

# from collections import deque

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# max_area = -1e9
# def bfs(x, y, now):
#     global max_area
#     queue = deque()
#     tmp_arr = []
#     tmp_arr.append((x, y))
#     queue.append((x, y))
#     visited = [[False] * n for _ in range(n)]
#     visited[x][y] = True
#     area = 1
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and visited[nx][ny] == False:
#                 if graph[nx][ny] == 0 or graph[nx][ny] == now:
#                     queue.append((nx, ny))
#                     tmp_arr.append((nx, ny))
#                     area += 1
#                     visited[nx][ny] = True
#     if max_area < area:
#         max_area = area
#         if max_area != 1:
#             return tmp_arr

# max_count = -1e9
# answer = 0
# remove = 0
# for i in range(n):
#     for j in range(n):
#         count = 0
#         block = bfs(i, j, graph[i][j])
#         if block != None:
#             count = len(block)
#             if count > max_count:
#                 remove = block
        
# if remove:
#     for x, y in remove:
#         graph[x][y] = -2
#     answer += len(remove) ** 2

# def gravity():
#     while True:
#         move = 0    
#         for i in range(n - 1):
#             for j in range(n):
#                 if graph[i][j] != -1 and graph[i+1][j] == -2:
#                     graph[i+1][j] = graph[i][j]
#                     graph[i][j] = -2
#                     move = 1
#         if move == 0:
#             break

# gravity()
# for i in graph:
#     print(i)
