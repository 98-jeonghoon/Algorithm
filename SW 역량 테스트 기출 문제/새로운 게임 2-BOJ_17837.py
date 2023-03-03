n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]
chess = []
for i in range(k):
    x, y, d = map(int, input().split())
    chess.append([x - 1, y - 1, d - 1])
    board[x - 1][y - 1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def change_dir(d):
    if d in [0 , 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d

def solve(horse_num):
    x, y, d = chess[horse_num]
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 2:
        d = change_dir(d)
        chess[horse_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 2:
            return True
    
    horse_up = []
    for h_idx, h_n in enumerate(board[x][y]):
        if h_n == horse_num:
            horse_up.extend(board[x][y][h_idx:])
            board[x][y] = board[x][y][:h_idx]
            break
    
    if graph[nx][ny] == 1:
        horse_up = horse_up[-1::-1]
        
    for h in horse_up:
        chess[h][0], chess[h][1] = nx, ny
        board[nx][ny].append(h)
    
    if len(board[nx][ny]) >= 4:
        return False
    return True

count = 0
while True:
    flag = False
    if count > 1000:
        print(-1)
        break
    for i in range(k):
        if solve(i) == False:
            flag = True
            break
    count += 1
    if flag:
        print(count)
        break