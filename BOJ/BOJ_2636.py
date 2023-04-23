from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited):
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                else:
                    graph[nx][ny] = 0

def count_cheese(graph, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
    return count

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

time = 0
last_cheese = 0

while True:
    cheese_count = count_cheese(graph, n, m)
    if cheese_count == 0:
        break
    last_cheese = cheese_count
    visited = [[False] * m for _ in range(n)]
    bfs(graph, visited)
    time += 1

print(time)
print(last_cheese)
