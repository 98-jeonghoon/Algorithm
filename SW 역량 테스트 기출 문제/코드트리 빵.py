from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dist = [[0] * n for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
people = [(-1, -1)] * m
store = []
for _ in range(m):
    x, y = map(int, input().split())
    store.append((x - 1, y - 1))
    
def ititialize_visited_dist():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            dist[i][j] = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    ititialize_visited_dist()
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if in_range(nx, ny) and visited[nx][ny] == False and graph[nx][ny] != 2:
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

time = 0

def simulate():
    for i in range(m):
        if people[i] == (-1, -1) or people[i] == store[i]:
            continue
        
        bfs(store[i][0], store[i][1])
        now_x, now_y = people[i]
        min_value = 1e9
        min_x, min_y = -1, -1
        
        for d in range(4):
            nx = now_x + dx[d]
            ny = now_y + dy[d]
            if in_range(nx, ny) and visited[nx][ny] == True and min_value > dist[nx][ny]:
                min_value = dist[nx][ny]
                min_x, min_y = nx, ny
        people[i] = (min_x, min_y)
        
    for i in range(m):
        if people[i] == store[i]:
            nx, ny = people[i]
            graph[nx][ny] = 2
    
    
    if time > m:
        return
    
    bfs(store[time - 1][0], store[time - 1][1])
    
    min_value = 1e9
    min_x, min_y = -1, -1
    for x in range(n):
        for y in range(n):
            if visited[x][y] == True and graph[x][y] == 1 and min_value > dist[x][y]:
                min_value = dist[x][y]
                min_x, min_y = x, y
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