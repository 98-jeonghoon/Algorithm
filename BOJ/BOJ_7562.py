from collections import deque

dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        if x == target_x and y ==target_y:
            return graph[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= map_size or ny >= map_size:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

n = int(input())
for _ in range(n):
    map_size = int(input())
    graph = [[0]*map_size for _ in range(map_size)]
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    print(bfs(x, y))