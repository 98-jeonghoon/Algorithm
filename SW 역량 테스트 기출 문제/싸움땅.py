n, m, k = map(int, input().split())
point = [0] * m

graph = [list(map(int, input().split())) for _ in range(n)]
gun_graph = [[[] for _ in range(n)] for _ in range(n)]
have_gun = [0] * m

# 초기 그래프의 gun 정보를 gun_graph로 업데이트 해줌
def init():
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                gun_graph[i][j].append(graph[i][j])


player_pos = []
player_ds = []

for _ in range(m):
    # x, y, 방향, 초기 스탯
    x, y, d, s = map(int, input().split())
    player_pos.append((x - 1, y - 1))
    player_ds.append([d, s])

# 방향 (상 우 하 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 공격력이 높은 총을 선택하는 함수
def choice_gun(x, y, idx):
    # 만약 해당칸에 총이 없다면 리턴
    if gun_graph[x][y] == []:
        return
    else:
        # 만약 내가 가진 총이 없다면
        if have_gun[idx] == 0:
            #가장 공격력이 높은것을 선택하기 위하여 정렬해줌
            gun_graph[x][y].sort()
            # pop연산을 통하여 공격력 높은 총 선택하고 해당 칸의 gun 지우기
            have_gun[idx] = gun_graph[x][y].pop()
        else:
            # 가지고 있는 gun을 변수에 담아주고 have_gun[idx]의 값을 0으로 초기화
            have = have_gun[idx]
            have_gun[idx] = 0
            # 가지고 있던 gun을 gun_graph에 넣고 정렬
            gun_graph[x][y].append(have)
            gun_graph[x][y].sort()
            have_gun[idx] = gun_graph[x][y].pop()

# 해당 칸에 총을 내려놓는 함수
def put_down_gun(loser):
    x, y = player_pos[loser]
    # 만약 가진 총이 없다면 리턴
    if have_gun[loser] == 0:
        return
    else:
        now = have_gun[loser]
        # 가진 총을 내려두기
        have_gun[loser] = 0
        gun_graph[x][y].append(now)


# 게임에서 진 플레이어가 이동하는 함수
def loser_move(loser):
    x, y = player_pos[loser]
    d = player_ds[loser][0]

    for i in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 격자를 벗어난다면 오른쪽으로 90도 회전
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            d = (d + 1) % 4
        # 해당 위치에 플레이어가 있다면 90도 회전
        elif (nx, ny) in player_pos:
            d = (d + 1) % 4
        else:
            # 해당 칸으로 이동하고 가장 공격력이 높은 총을 선택
            player_pos[loser] = (nx, ny)
            player_ds[loser][0] = d
            choice_gun(nx, ny, loser)
            return

# 현재플레이어 i와 해당 칸에 있던 플레이어 idx의 싸움을 진행하는 함수
def fight(i, idx):
    # 현재 플레이어의 공격력 정보 now_player, 해당 칸에 있던 플레이어 공격력 정보 next_player
    # 초기 능력치와 가지고 있는 총의 공격력 합을 비교해야함
    now_player = player_ds[i][1] + have_gun[i]
    next_player = player_ds[idx][1] + have_gun[idx]
    if now_player > next_player:
        winner, loser = i, idx
    elif now_player == next_player:
        # 만약 수치가 같으면 초기 능력치를 비교해야됨
        if player_ds[i][1] > player_ds[idx][1]:
            winner, loser = i, idx
        else:
            winner, loser = idx, i
    else:
        winner, loser = idx, i

    # 이긴 사람이 점수를 획득한다.
    point[winner] += abs(now_player - next_player)

    # 승자와 패자가 결정됐다면, 진 플레이어와 이긴플레이어 각각 정해진 함수 수행
    # 패자는 현재 총을 가지고 있다면 해당 칸에 내려두고 이동한다.
    put_down_gun(loser)
    loser_move(loser)
    # 승자는 총을 선택한다.
    x, y = player_pos[winner]
    choice_gun(x, y, winner)


# 1-1
def player_move():
    # 첫번째 플레이어부터 순차적으로 본인이 향하고 있는 방향만큼 이동함
    for i in range(len(player_pos)):
        x, y = player_pos[i]
        d = player_ds[i][0]
        nx = x + dx[d]
        ny = y + dy[d]
        # 만약 범위를 벗어나면 정반대 방향으로 방향을 바꾸어 1만큼 이동
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            # 방향을 바꿔주는 로직
            if d in [0, 1]:
                d += 2
            else:
                d -= 2
            # 방향이 바뀌었으면 해당 방향으로 다시 nx, ny를 설정
            nx = x + dx[d]
            ny = y + dy[d]

        # 해당 칸에 총이 있는지 확인한다.
        # 만약 이동한 칸에 플레이어가 있다면 싸움 진행
        if (nx, ny) in player_pos:
            # 싸워야 하는 플레이어의 index값을 가져온다
            idx = player_pos.index((nx, ny))
            # 플레이어를 이동시킨다
            player_pos[i] = (nx, ny)
            # 방향 초기화
            player_ds[i][0] = d
            # 두 플레이어의 싸움 진행
            fight(i, idx)

        # 없다면 해당 칸으로 이동하고, 놓여있는 총과 플레이어가 가지고 있는 총중에 가장 큰 값을 선택
        else:
            # 해당 플레이어의 위치를 초기화
            player_pos[i] = (nx, ny)
            # 방향 초기화
            player_ds[i][0] = d
            # 총을 선택
            choice_gun(nx, ny, i)

# 초기 설정
init()

# 시뮬레이션 진행
for i in range(k):
    player_move()

print(*point)