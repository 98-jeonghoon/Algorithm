from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

store = []
for _ in range(m):
    x, y = map(int, input().split())
    store.append((x - 1, y - 1))

people = [(-1, -1)] * m
dx = [-1, 0 ,0, 1]
dy = [0, -1, 1, 0]

from collections import deque

# def initalize_visited():
#     for i in range(n):
#         for j in range(n):
#             visited[i][j] = False

dist = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
def bfs(pos):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            dist[i][j] = 0
    x, y = pos
    dist[x][y] = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] != 2:
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

time = 0

def simulate():
    for i in range(m):
        if people[i] == (-1, -1) or people[i] == store[i]:
            continue

        bfs(store[i])

        px, py = people[i]

        min_dist = 1e9
        min_x, min_y = -1, -1

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == True and min_dist > dist[nx][ny]:
                min_dist = dist[nx][ny]
                min_x, min_y = nx, ny
            
        people[i] = (min_x, min_y)
    
    for i in range(m):
        if people[i] == store[i]:
            x, y = people[i]
            graph[x][y] = 2

    if time > m:
        return
    
    bfs(store[time - 1])

    min_dist = 1e9
    min_x, min_y = -1, -1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True and graph[i][j] == 1 and min_dist > dist[i][j]:
                min_dist = dist[i][j]
                min_x, min_y = i, j
    
    people[time - 1] = (min_x, min_y)
    graph[min_x][min_y] = 2

def end():
    for i in range(m):
        if people[i] != store[i]:
            return False
    return True

while True:
    time += 1
    simulate()
    if end():
        break

print(time)
