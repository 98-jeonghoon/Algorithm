import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]
def dfs(x,y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)
            
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
                
    print(count)
    
    
# from collections import deque

# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y =queue.popleft()
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
#     for _ in range(h):
#         graph.append(list(map(int, input().split())))
#     result = 0
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1:
#                 result += 1
#                 bfs(i, j)
#     print(result)