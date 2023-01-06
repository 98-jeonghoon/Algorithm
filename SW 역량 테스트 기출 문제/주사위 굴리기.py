n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int ,input().split()))
dice = [0, 0, 0, 0, 0, 0]

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def roll(dir):
    if dir == 1: #동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2: #서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3: #북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else: #남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

for i in move:
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    roll(i)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])