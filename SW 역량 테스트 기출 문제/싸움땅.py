n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
gun = [[[] for _ in range(n)] for _ in range(n)]
player_gun = [0] * m
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            gun[i][j].append(graph[i][j])

player_dp = []
player_pos = []
score = [0] * m
for _ in range(m):
    x, y, d, s = map(int, input().split())
    player_pos.append((x - 1, y - 1))
    player_dp.append([d, s])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change_gun(nx, ny, idx):
    if gun[nx][ny] == []:
        return
    else:
        if player_gun[idx] == 0:
            gun[nx][ny].sort()
            now_gun = gun[nx][ny].pop()
            player_gun[idx] = now_gun
        else:
            gun[nx][ny].append(player_gun[idx])
            gun[nx][ny].sort()
            now_gun = gun[nx][ny].pop()
            player_gun[idx] = now_gun

def put_down_gun(loser):
    x, y = player_pos[loser]
    if player_gun[loser] == 0:
        return
    else:
        gun[x][y].append(player_gun[loser])
        player_gun[loser] = 0
        
def fight(i, idx):
    if player_dp[i][1] + player_gun[i] > player_dp[idx][1] + player_gun[idx]:
        winner, loser = i, idx
    elif player_dp[i][1] + player_gun[i] < player_dp[idx][1] + player_gun[idx]:
        winner, loser = idx, i
    else:
        if player_dp[i][1] > player_dp[idx][1]:
            winner, loser = i, idx
        else:
            winner, loser = idx, i

    score[winner] += abs((player_dp[i][1] + player_gun[i]) - (player_dp[idx][1] + player_gun[idx]))

    put_down_gun(loser)

    # looser move
    x, y = player_pos[loser]
    d = player_dp[loser][0]
    for i in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            d = (d + 1) % 4
        elif (nx, ny) in player_pos:
            d = (d + 1) % 4
        else:
            player_pos[loser] = (nx, ny)
            player_dp[loser][0] = d
            change_gun(nx, ny, loser)
            break
    x, y = player_pos[winner]
    change_gun(x, y, winner)

def player_move():
    for i in range(len(player_pos)):
        x, y = player_pos[i]
        d = player_dp[i][0]
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            if d < 2:
                d = d + 2
            else:
                d = d - 2
            nx = x + dx[d]
            ny = y + dy[d]
        if (nx, ny) in player_pos:
            idx = player_pos.index((nx, ny))
            player_pos[i] = (nx, ny)
            player_dp[i][0] = d
            fight(i, idx)
        else:
            player_pos[i] = (nx, ny)
            player_dp[i][0] = d
            change_gun(nx, ny, i)

for i in range(k):
    player_move()

for i in score:
    print(i, end=' ')