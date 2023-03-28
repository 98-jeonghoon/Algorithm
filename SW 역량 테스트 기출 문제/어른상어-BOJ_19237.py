n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

directions = list(map(int, input().split()))

priorities = [[] * m for _ in range(m)]
for i in range(m):
    for _ in range(4):
        priorities[i].append(list(map(int, input().split())))

# 상어 번호 / 남은 냄새 시간
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if graph[i][j] != 0:
                smell[i][j] = [graph[i][j], k]


def move():
    tmp_graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:
                direction = directions[graph[x][y] - 1]
                flag = False
                for d in range(4):
                    nx = x + dx[priorities[graph[x][y] - 1][direction - 1][d] - 1]
                    ny = y + dy[priorities[graph[x][y] - 1][direction - 1][d] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            directions[graph[x][y] - 1] = priorities[graph[x][y] - 1][direction- 1][d]
                            if tmp_graph[nx][ny] == 0:
                                tmp_graph[nx][ny] = graph[x][y]
                            else:
                                tmp_graph[nx][ny] = min(tmp_graph[nx][ny], graph[x][y])
                            flag = True
                            break
                if flag:
                    continue
                for index in range(4):
                    nx = x + dx[priorities[graph[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[graph[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == graph[x][y]:
                            directions[graph[x][y] - 1] = priorities[graph[x][y] - 1][direction - 1][index]
                            tmp_graph[nx][ny] = graph[x][y]
                            break
    return tmp_graph

time = 0
while True:
    update_smell()
    tmp_graph = move()
    graph = tmp_graph
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                check = False
    if check:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break