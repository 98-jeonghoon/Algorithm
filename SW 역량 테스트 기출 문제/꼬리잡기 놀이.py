n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def detect_line(sx, sy):
    teammates = [(sx, sy)]
    x, y = sx, sy
    while graph[x][y] != 3:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not in_range(nx, ny):
                continue
            if len(teammates) >= 2 and (nx, ny) == teammates[-2]:
                continue
            if graph[x][y] == 1 and graph[nx][ny] == 3:
                continue
            if graph[nx][ny] not in [2, 3]:
                continue
            x, y = nx, ny
            break
        teammates.append((x, y))
    return teammates

    
    
def detect_whole_team():
    team = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                team.append(detect_line(i, j))
    return team

def move_one_team(teamates):
    x, y = teamates[0]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not in_range(nx, ny):
            continue
        if graph[nx][ny] not in [3, 4]: continue
        break
    
    new_pos = []
    for teamate in teamates:
        cx, cy = teamate
        new_pos.append((nx, ny))
        nx, ny = cx, cy
        graph[cx][cy] = 4
    
    for idx, (x, y) in enumerate(new_pos):
        if idx == 0:
            graph[x][y] = 1
        elif idx == len(new_pos) - 1:
            graph[x][y] = 3
        else:
            graph[x][y] = 2

def move_while_teams():
    teams = detect_whole_team()
    
    for teamates in teams:
        move_one_team(teamates)

def throw_ball(round_num):
    # 공을 조건에 맞게 던지고, 충돌하는 좌표를 돌려주기
    round_num %= n * 4
    if round_num < n:
        x1, y1 = round_num, 0
        x2, y2 = round_num, n
    elif round_num < n * 2:
        x1, y1 = n - 1, round_num - n
        x2, y2 =    -1, round_num - n
    elif round_num < n * 3:
        x1, y1 = (3 * n - 1) - round_num, n - 1
        x2, y2 = (3 * n - 1) - round_num, -1
    else:
        x1, y1 = 0, (4 * n - 1) - round_num
        x2, y2 = n, (4 * n - 1) - round_num
    
    dx, dy = (x2 - x1) // n, (y2 - y1) // n
    x, y = x1, y1
    while (x, y) != (x2, y2):
        if graph[x][y] not in [0, 4]:
            return (x, y)
        x, y = x + dx, y + dy
    return None

def calc(coord):
    teams = detect_whole_team()
    for teammates in teams:
        for idx, teammate in enumerate(teammates, 1):
            if teammate == coord:
                x1, y1 = teammates[0]
                x2, y2 = teammates[-1]
                graph[x1][y1], graph[x2][y2] = graph[x2][y2], graph[x1][y1]
                return idx * idx
            
answer = 0
for round_num in range(k):
    move_while_teams()
    coord = throw_ball(round_num)
    if coord is None:
        continue
    answer += calc(coord)

print(answer)