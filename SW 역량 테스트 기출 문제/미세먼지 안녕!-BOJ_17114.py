r, c ,t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
air_clean = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            air_clean.append((i, j))

def diffusion():
    arr = []
    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                arr.append((i, j))
    for x, y in arr:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] == -1:
                continue
            dust = graph[x][y] // 5
            tmp_arr[nx][ny] += dust
            tmp_arr[x][y] -= dust
        nx, ny = 0, 0
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += tmp_arr[i][j]

def top_clean():
    # 동 북 서 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_clean[0][0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_clean[0][0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

def bottom_clean():
    # 동 남 서 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_clean[1][0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_clean[1][0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

for _ in range(t):
    diffusion()
    top_clean()
    bottom_clean()
    
answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]
            
print(answer)
