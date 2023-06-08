# from itertools import combinations
# from collections import deque
# import copy

# # 설계
# # 1. 궁수 3명을 배치해야된다. 백트래킹으로 궁수를 배치하는 모든 경우의 수를 체크한다.
# # 2. 거리가 D이하인 적중에 가장 가까운 적을 공격한다. dist를 이용하여 가장 가까운애를 선택한다.
# # 3. 적이 한칸 아래로 이동한다. 모든 적이 격자판에서 제외되면 게임이 끝난다.


# n, m, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# # 궁수의 위치를 위한 배열을 추가해줌
# graph.append([0] * m)
# answer = 0

# def bfs(arrow_pos):
#     # 우선순위가 왼쪽이 가장 높음
#     # 좌 우 상 하 기준 탐색
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     cnt = 0
#     for pos_x, pos_y in arrow_pos:
#         dist = [[-1] * m for _ in range(n + 1)]
#         check = [[False] * m for _ in range(n + 1)]
#         check[pos_x][pos_y] = True
#         queue = deque()
#         queue.append((pos_x, pos_y))
#         dist[pos_x][pos_y] = 0
#         while queue:
#             x, y = queue.popleft()     
#             for dir in range(4):
#                 nx = x + dx[dir]
#                 ny = y + dy[dir]
#                 if 0 <= nx < n and 0 <= ny < m:
#                     if check[nx][ny] == False:
#                         dist[nx][ny] = dist[x][y] + 1
#                         check[nx][ny] = True
#                         queue.append((nx, ny))
        
#         min_x, min_y = 0, 0
#         min_value = 1e9
#         for move in range(1, d + 1):
#             for dir in range(4):
#                 min_nx = pos_x + (dx[dir] * move)
#                 min_ny = pos_y + (dy[dir] * move)
#                 if 0 <= min_nx < n and 0 <= ny < m:
#                     if graph[min_nx][min_ny] == 1 and check[min_nx][min_ny] == True and dist[min_nx][min_ny] < min_value:
#                         min_value = dist[min_nx][min_ny]
#                         min_x, min_y = min_nx, min_ny
    
#         if graph[min_x][min_y] == 1:
#             graph[min_x][min_y] = 0
#             cnt += 1
#     return cnt
                    
# def PRINT_GRAPH():
#     for i in graph:
#         print(i)

# def end():
#     # 적이 하나라도 남아있으면 게임이 안끝남
#     res = 0
#     for i in graph:
#         res += i.count(1)
#     if res == 0:
#         return False
#     else:
#         return True

# # 적이 아래로 한칸 내려오는 로직
# def move_down():
#     # 새로운 배열을 하나 만들어주고
#     tmp_graph = [[0] * m for _ in range(n)]
#     # 전체를 탐색하면서 한칸 내려간 값을 tmp 그래프에 담아줌
#     for i in range(n):
#         for j in range(m):
#             if i + 1 >= n:
#                 continue
#             tmp_graph[i + 1][j] = graph[i][j]
    
#     # tmp그래프의 값을 그대로 원래 그래프에 옮겨주기
#     for x in range(n):
#         for y in range(m):
#             graph[x][y] = tmp_graph[x][y]

# visited = [False] * m
# arrow_pos = []

# def back_tracking(depth, idx):
#     global answer
#     if depth == 3:
#         cnt = 0
#         while True:
#             if not end():
#                 break
#             cnt += bfs(arrow_pos)
#             move_down()
#         answer = max(answer, cnt)
#         return

    
#     for i in range(idx, m):
#         # 만약 궁수를 배치할수 있으면
#         if graph[n][i] == 0 and not visited[i]:
#             # 궁수를 배치한다
#             graph[n][i] = 2
#             # 방문처리를 해주고
#             visited[i] = True
#             # arrow_pos 궁수의 위치를 배열에 넣어줌
#             arrow_pos.append((n, i))
#             back_tracking(depth + 1, i + 1)
#             # 백트래킹에서 탈출했다면 궁수 자리를 다시 빈칸으로 만듬
#             graph[n][i] = 0
#             # 궁수의 위치를 pop한다
#             arrow_pos.pop()
#             # 방문해제
#             visited[i] = False

# back_tracking(0, 0)
# print(answer)
# # PRINT_GRAPH()
from itertools import combinations
from collections import deque
import copy

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph.append([0] * m)
answer = 0

def attack(arrow_pos, graph):
    cnt = 0
    targets = []
    for pos_x, pos_y in arrow_pos:
        enemies = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    enemies.append((i, j))
        enemies.sort(key=lambda x: (abs(x[0]-pos_x) + abs(x[1]-pos_y), x[1]))
        if enemies and abs(enemies[0][0]-pos_x) + abs(enemies[0][1]-pos_y) <= d:
            targets.append(enemies[0])
    targets = list(set(targets))

    for target in targets:
        if graph[target[0]][target[1]] == 1:
            graph[target[0]][target[1]] = 0
            cnt += 1
    return cnt

def end(graph):
    res = 0
    for i in graph:
        res += i.count(1)
    if res == 0:
        return False
    else:
        return True

def move_down(graph):
    tmp_graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i + 1 >= n:
                continue
            tmp_graph[i + 1][j] = graph[i][j]
    for x in range(n):
        for y in range(m):
            graph[x][y] = tmp_graph[x][y]

def back_tracking(depth, idx, arrow_pos):
    global answer
    if depth == 3:
        tmp_graph = copy.deepcopy(graph)
        cnt = 0
        while True:
            if not end(tmp_graph):
                break
            cnt += attack(arrow_pos, tmp_graph)
            move_down(tmp_graph)
        answer = max(answer, cnt)
        return

    for i in range(idx, m):
        if graph[n][i] == 0:
            graph[n][i] = 2
            arrow_pos.append((n, i))
            back_tracking(depth + 1, i + 1, arrow_pos)
            graph[n][i] = 0
            arrow_pos.pop()

back_tracking(0, 0, [])
print(answer)
