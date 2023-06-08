from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate_cross(graph):
    # 옮겨 담을 그래프 선언
    tmp_graph = [[0] * n for _ in range(n)]

    # 그래프 전체를 반시계 방향으로 90도 회전시킴
    graph = list(map(list, zip(*graph)))[::-1]
    # 회전시킨 그래프의 십자가 모양을 tmp_graph에 옮겨담음
    # 가로줄, 세로줄
    x, y = n // 2, n // 2
    
    # 세로줄 먼저 옮겨담기
    # x좌표는 아래로 한칸 내려가면서 y좌표는 고정
    for i in range(n):
        tmp_graph[i][y] = graph[i][y]
    
    # 가로줄 옮겨담기
    # x좌표는 그대로 y좌표만 한칸씩 이동
    # tmp_graph[x] = graph[x] -> 이렇게 선언해도 상관없음
    for i in range(n):
        tmp_graph[x][i] = graph[x][i]
    
    # for i in tmp_graph:
    #     print(i)

    # 원본 그래프를 다시 원복하기
    graph = list(map(list, zip(*graph[::-1])))

    # 십자를 제외한 나머지 값들을 완전탐색하면서 tmp_graph에 채워주기
    for i in range(n):
        for j in range(n):
            # 칸에 있는 숫자는 항상 0 이상이니 빈칸은 0임
            if tmp_graph[i][j] == 0:
                tmp_graph[i][j] = graph[i][j]

    return tmp_graph


def init_graph(graph):
    # 그래프를 전체 0으로 초기화하는 함수
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j] = 0
    # return graph


def rotate_square(graph):
    # 정사각형 4개를 뒤집어야함
    # 옮겨 담을 그래프 선언
    tmp_graph = [[0] * n for _ in range(n)]

    x, y = n // 2, n // 2

    # 왼상, 우상, 왼하, 우하 차례대로 1~4분면이라 칭하겠음
    # 1사분면
    for i in range(x):
        for j in range(y):
            tmp_graph[j][(n // 2) - 1 - i] = graph[i][j]
    
    # 2사분면
    for i in range(x):
        for j in range(y + 1, n):
            tmp_graph[j - (n//2) - 1][n - 1 - i] = graph[i][j]

    # 3사분면
    for i in range(x + 1, n):
        for j in range(y):
            tmp_graph[j + (n // 2) + 1][n - 1 - i] = graph[i][j]

    # 4사분면
    for i in range(x + 1, n):
        for j in range(y + 1, n):
            tmp_graph[j][(n//2) + 1 - 1 - i] = graph[i][j]
    
    # 십자가 모양은 그대로 옮겨주기
    for i in range(n):
        for j in range(n):
            if i == x or y == j:
                tmp_graph[i][j] = graph[i][j]
    # for i in tmp_graph:
    #     print(i)
    return tmp_graph


dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs(x, y, num):
    queue = deque()
    # 현 좌표 방문체크
    visited[x][y] = True
    # 해당 그룹의 칸의 수를 한칸 카운팅
    group_cnt[num] += 1
    # 전처리
    group[x][y] = num
    queue.append((x, y))

    # bfs진행
    while queue:
        x, y, = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    group[nx][ny] = num
                    group_cnt[num] += 1


def score():
    cnt = 0
    for x in range(n):
        for y in range(n):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and group[x][y] != group[nx][ny]:
                    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
                    diff1, diff2 = group[x][y], group[nx][ny]
                    value1, value2 = graph[x][y], graph[nx][ny]
                    grp_cnt1, grp_cnt2 = group_cnt[diff1], group_cnt[diff2]
                    cnt += (grp_cnt1 + grp_cnt2) * value1 * value2
    return cnt // 2

answer = 0

for _ in range(4):
    visited = [[False] * n for _ in range(n)]
    # 그룹을 다시 정의해줌
    group = [[0] * n for _ in range(n)]
    # 각 그룹에 해당되는 칸의 수를 인덱스 기준으로 cnt하기 위한 배열선언
    group_cnt = [0] * (n * n + 1) 
    # 그룹을 세기위한 변수선언
    group_num = 0

    for i in range(n):
        for j in range(n):
            # 만약 방문하지 않았다면
            if visited[i][j] == False:
                # 그룹을 하나 추가해주고
                group_num += 1
                # bfs돌리기
                bfs(i, j, group_num)
    

    answer += score()
    graph = rotate_cross(graph)
    graph = rotate_square(graph)

print(answer)