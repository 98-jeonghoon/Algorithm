from collections import deque
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [1, 2, 3, 4, 5, 6]

def move_dice(dir):
    if dir == 0: #동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1: #남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif dir == 2: #서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else: #북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]


def change_dir(d):
    if d == 0:
        d = 2
    elif d == 1:
        d = 3
    elif d == 2:
        d = 0
    elif d == 3:
        d = 1
    return d


def bfs(x, y, now):
    queue = deque()
    queue.append((x, y))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == now:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
    return count

x, y, d, score = 0, 0, 0, 0

for test in range(k):
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        d = change_dir(d)
        nx = x + dx[d]
        ny = y + dy[d]
    score += bfs(nx, ny, graph[nx][ny]) * graph[nx][ny]
    move_dice(d)
    if dice[5] > graph[nx][ny]:
        d = (d - 3) % 4
    elif dice[5] < graph[nx][ny]:
        d = (d + 3) % 4
    elif dice[5] == graph[nx][ny]:
        pass
    
    x, y = nx, ny
    
print(score)
    
        

