from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
last_attacked = [[0] * m for _ in range(n)]
is_attack = [[False] * m for _ in range(n)]


def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                cnt += 1
    return cnt == 1

def attacker() -> tuple:
    min_value = 1e9
    attacker_arr = []
    # 공격력이 가장 낮은 값 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            else:
                # 해당 값을 발견하면 min_value 값으로 바꿔주기
                if min_value > graph[i][j]:
                    min_value = graph[i][j]

    #해당 공격력인 칸 좌표 선택해서 attack_arr에 저장하기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == min_value:
                attacker_arr.append((i, j, last_attacked[i][j]))
    
    # 조건에 맞게 정렬 해줌
    # 정렬 조건 (가장 최근에 공격, 행과 열의 합 큰, 열 값이 가장 큰)
    attacker_arr.sort(key=lambda x : ((x[2], x[0] + x[1], x[1])), reverse= True)
    
    # attaker_pos의 x, y 좌표를 반환해줌
    return attacker_arr[0][0], attacker_arr[0][1]

def target() -> tuple:
    # attacker와 같이 구현
    max_value = -1
    target_arr = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            else:
                if graph[i][j] > max_value:
                    max_value = graph[i][j]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == max_value:
                target_arr.append((i, j, last_attacked[i][j]))
    
    # 조건에 맞게 정렬
    # 공격한지 오래된 포탑, 행과 열이 합이 작은, 열 값이 가장 작은 순
    target_arr.sort(key=lambda x : (x[2], (x[0] + x[1]), x[1]))

    return target_arr[0][0], target_arr[0][1]


def attack(x, y, attack_power):
    # 공격한걸 기록해줌
    is_attack[x][y] = True
    # 해당 좌표를 attack_power만큼 공격함
    graph[x][y] -= attack_power
    
    # 만약 0보다 작으면 0으로 맞춰주기
    if graph[x][y] < 0:
        graph[x][y] = 0
    
def raiser_attack(attacker_pos, traget_pos):
    visited = [[False] * m for _ in range(n)]
    
    # Back Trace를 위한 배열 선언
    come = [[None] * m for _ in range(n)]
    # 4개 방향으로 탐색한다
    # 우선순위 -> (우, 하, 좌, 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque()
    queue.append(attacker_pos)
    visited[attacker_pos[0]][attacker_pos[1]] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            # 격자가 이어짐
            nx = (x + dx[d]) % n
            ny = (y + dy[d]) % m
            if visited[nx][ny] == False and graph[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                # 역추적을 위해 전에 온 좌표를 기록해줌
                come[nx][ny] = (x, y)
    
    # for i in come:
    #     print(i)

    if visited[target_pos[0]][target_pos[1]] == False:
        return False
    
    attacker_x, attacker_y = attacker_pos
    x, y = target_pos
    
    # 공격 진행
    while x != attacker_x or y != attacker_y:
        # 공격 루트는 공격력 // 2 만큼
        attack_power = graph[attacker_x][attacker_y] //2

        # 해당 공격 좌표는 공격력 만큼
        if x == target_pos[0] and y == target_pos[1]:
            attack_power = graph[attacker_x][attacker_y]
        
        # 공격하기
        attack(x, y, attack_power)

        # 역추적하기
        x, y = come[x][y]
    
    return True



def potan_attack(attack_pos, target_pos):
    # 대각선을 포함한 8개의 값
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    # 타겟을 바로 공격함
    x, y = target_pos
    # 공격력은 그대로 적용
    attack_power = graph[attack_pos[0]][attack_pos[1]]
    attack(x, y, attack_power)
    
    # 타겟 주위 8방향을 공격함.
    for d in range(8):
        # 격자가 이어져있음
        nx = (x + dx[d]) % n
        ny = (y + dy[d]) % m
        # 좌표가 공격자이면 무시해야됨
        if nx == attack_pos[0] and ny == attack_pos[1]:
            continue
        # 공격력의 반만큼 공격함
        attack_power = graph[attack_pos[0]][attack_pos[1]] // 2
        attack(nx, ny, attack_power)

# 포탑 정비하기
def repair():
    for i in range(n):
        for j in range(m):
            if is_attack[i][j] == False and graph[i][j] != 0:
                graph[i][j] += 1



for time in range(1, k + 1):
    # 만약 종료 조건을 만족한다면 바로 종료
    if check():
        break

    # 공격자 좌표 얻어옴
    attack_pos = attacker()
    
    # 타겟 좌표를 얻어옴
    target_pos = target()

    # 핸디캡을 부여함
    graph[attack_pos[0]][attack_pos[1]] += n + m

    # 공격시간을 갱신
    last_attacked[attack_pos[0]][attack_pos[1]] = time

    # 공격을 체크하는 배열 선언
    is_attack = [[False] * m for _ in range(n)]
    is_attack[attack_pos[0]][attack_pos[1]] = True

    # 레이저 공격 시작
    if not raiser_attack(attack_pos, target_pos):
        #레이저 공격이 안된다면 포탄던지기
        potan_attack(attack_pos, target_pos)

    # 정비하기
    repair()

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, graph[i][j])

print(answer)
# for i in graph:
#     print(i)
'''
4 4 1
0 1 4 4
8 0 10 13
8 0 11 26
0 0 0 0
'''