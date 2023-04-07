n, m, k = map(int, input().split())
gun = [[[] for _ in range(n)] for _ in range(n)]

EMPTY = (-1, -1, -1, -1, -1, -1)
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        if num[j] != 0:
            gun[i][j].append(num[j])

players = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

score = [0] * m
for i in range(m):
    x, y, d, s = map(int, input().split())
    players.append((i, x - 1, y - 1, d, s, 0))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_player(pos):
    for i in range(m):
        x, y = players[i][1], players[i][2]
        if pos == (x ,y):
            return players[i]
    return EMPTY

def next_move(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]

    if not in_range(nx, ny):
        if d < 2:
            d = d + 2
        else:
            d = d - 2
        nx = x + dx[d]
        ny = y + dy[d]
    
    return (nx, ny, d)

def update(p):
    num, x, y, d, s, a = p

    for i in range(m):
        num1, x1, y1, d1, s1, a1 = players[i]
        if num1 == num:
            players[i] = p
            break

def move(p, pos):
    num, x, y, d, s, a = p
    nx, ny = pos

    gun[nx][ny].append(a)
    gun[nx][ny].sort(reverse=True)
    a = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    p = (num, nx, ny, d, s, a)
    update(p)


def lose_user_move(p):
    num, x, y, d, s, a =p
    gun[x][y].append(a)
    for i in range(4):
        direct = (d + i) % 4
        nx = x + dx[direct]
        ny = y + dy[direct]
        if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, direct, s, 0)
            move(p, (nx, ny))
            break
    
def duel(p1, p2, pos):
    num1, x1, y1, d1, s1, a1 = p1
    num2, x2, y2, d2, s2, a2 = p2

    if (s1 + a1, s1) > (s2 + a2, s2):
        score[num1] += (s1 + a1) - (s2 + a2)
        lose_user_move(p2)
        move(p1, pos)
    else:
        score[num2] += (s2 + a2) - (s1 + a1)
        lose_user_move(p1)
        move(p2, pos)

def simulate():
    for i in range(m):
        num, x, y, d, s, a = players[i]
        nx, ny, ndir = next_move(x, y, d)

        next_player = find_player((nx, ny))

        curr_player = (num, nx, ny, ndir, s, a)
        update(curr_player)

        if next_player == EMPTY:
            move(curr_player, (nx, ny))
        else:
            duel(curr_player, next_player, (nx, ny))

for i in range(k):
    simulate()

for point in score:
    print(point, end=' ')