# 격자크기, 박멸이 진행되는 년 수, 확산 범위, 남아있는 년수
n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 정답
answer = 0

# 상 하 좌 우
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

# 제초제가 뿌려져있는지 체크하기 위한 배열 / 0 이면 제초제가 뿌려져있지 않은것임
death_graph = [[0] * n for _ in range(n)]

def print_graph():
    for i in graph:
        print(i)

def step_one():
    # 완전 탐색을 진행
    for i in range(n):
        for j in range(n):
            # 만약 해당 칸에 나무가 있다면
            if graph[i][j] > 0:
                # 인접한 나무 개수를 체크하기 위한 cnt 변수 선언
                cnt = 0
                # 4방향을 체크
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    # 범위를 벗어나지 않고, 나무가 있다면 cnt += 1
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                        cnt += 1
                # 해당 칸에 인접한 나무 개수만큼 더해줌
                if cnt != 0:
                    graph[i][j] += cnt
    
    # print_graph()

# step_one()
def step_two():
    # 번식 작업을 처리해주기 위한 tmp_graph 선언
    tmp_graph = [[0] * n for _ in range(n)]
    
    # 완전탐색을 진행하며
    for x in range(n):
        for y in range(n):
            # 해당칸에 나무가 있다면
            if graph[x][y] > 0:
                # 비어있는 칸을 조사하기 위한 cnt, put 선언
                cnt, put = 0, []
                # 4방향 탐색을 진행한다.
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 벽, 다른나무, 제초제 모두 없는 칸에 번식을 진행한다.
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and death_graph[nx][ny] == 0:
                        # 해당 칸의 개수 세기
                        cnt += 1
                        # 해당 칸의 좌표 기록
                        put.append((nx, ny))
                # 번식할 나무 개수 구하기
                if cnt != 0:
                    tree = graph[x][y] // cnt
                    # 번식할 칸에 나무 개수만큼 더해주기
                    for put_x, put_y in put:
                        tmp_graph[put_x][put_y] += tree
    
    # for i in tmp_graph:
    #     print(i)
    
    # 번식한 나무 graph와 원본 graph 합쳐주기
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] != 0:
                graph[i][j] += tmp_graph[i][j]
    
    # print_graph()
                        



# 나무를 죽이는 작업
def step_tree():
    global answer
    # 가장 많은 나무를 죽이는 칸을 구하기 위한 max_graph선언
    max_graph = [[0] * n for _ in range(n)]
    # 대각선 방향
    # 좌상, 우상, 좌하, 우하
    d_dx = [-1, -1, 1, 1]
    d_dy = [-1, 1, -1, 1]
    
    # 죽이는 나무를 구하기 위한 완전탐색 진행
    for x in range(n):
        for y in range(n):
            # 만약 해당칸에 나무가 있다면
            if graph[x][y] > 0:
                # 해당 칸의 나무를 추가해주고
                max_graph[x][y] += graph[x][y]
                # 4방향을 돌면서
                for d in range(4):
                    # k만큼 이동한다
                    for move in range(1, k + 1):
                        nx = x + d_dx[d] * move
                        ny = y + d_dy[d] * move
                        if 0 <= nx < n and 0 <= ny < n:
                            # 만약 나무가 없거나 벽을 만난다면 중단한다.
                            if graph[nx][ny] == 0 or graph[nx][ny] == -1:
                                break
                            # 해당칸에 해당하는 나무를 추가해준다.
                            max_graph[x][y] += graph[nx][ny]
    
    # for i in max_graph:
    #     print(i)

    # 가장 많이 죽이는 칸의 값과 좌표를 구해야함.
    tmp_x, tmp_y = 0, 0
    max_value = -1e9
    
    for x in range(n):
        for y in range(n):
            if max_graph[x][y] > max_value:
                max_value = max_graph[x][y]
                tmp_x, tmp_y = x, y
    
    # 정답 구하기
    answer += max_value
    
    # 제초제 뿌리기
    death_graph[tmp_x][tmp_y] = c + 1
    graph[tmp_x][tmp_y] = 0

    for d in range(4):
        for move in range(1, k + 1):
            nx = tmp_x + d_dx[d] * move
            ny = tmp_y + d_dy[d] * move
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == -1:
                    break
                if graph[nx][ny] == 0:
                    death_graph[nx][ny] = c + 1
                    graph[nx][ny] = 0
                    break
                
                death_graph[nx][ny] = c + 1
                graph[nx][ny] = 0
    
    # for i in death_graph:
    #     print(i)
                            


# 제초제가 1년 지날때마다 사라지는 함수
def step_four():
    for i in range(n):
        for j in range(n):
            if death_graph[i][j] > 0:
                death_graph[i][j] -= 1

for _ in range(m):
    step_one()
    step_two()
    step_tree()
    step_four()
print(answer)