from collections import deque
m , n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

