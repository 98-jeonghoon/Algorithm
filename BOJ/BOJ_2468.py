from collections import deque

n = int(input())
graph = []
max_num = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > max_num:
            max_num = graph[i][j]
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, rain):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > rain and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                
result = 0
for i in range(max_num):
    visited = [[0] * n for i in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                count += 1
    if result < count:
        result = count
        
print(result)