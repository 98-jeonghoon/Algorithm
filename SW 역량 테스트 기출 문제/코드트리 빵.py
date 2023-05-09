from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
store = []
people_pos = [(-1, -1)] * m

for _ in range(m):
    x, y = map(int, input().split())
    store.append((x - 1, y - 1))

# 방향 우선순위 설정 (상 좌 우 하)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


# 편의점, 베이스캠프를 지날수있는지 확인하기 위하여 배열선언
check_visited = [[False] * n for _ in range(n)]

# 최단경로를 구하기 위한 bfs
def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 격자를 벗어나지 않고, 방문하지 않았으면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                # 편의점, 베이스캠프를 경유할수 있다면
                if check_visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
    return dist, visited


# 시뮬레이션이 종료되는지 확인하는 함수
def check():
    for i in range(m):
        # 만약 편의점 좌표랑 사람의 좌표가 하나라도 다르면 False 리턴
        if store[i] != people_pos[i]:
            return False
    # 모두 동일하다면 True 리턴
    else:
        return True
    

time = 0
def simulate():
    for i in range(m):
        if people_pos[i] == (-1, -1) or people_pos[i] == store[i]:
            continue
        dist, visited = bfs(store[i][0], store[i][1])
        now_x, now_y = people_pos[i]
        min_value = 1e9
        min_x, min_y = -1, -1

        for d in range(4):
            nx = now_x + dx[d]
            ny = now_y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == True and check_visited[nx][ny] == False and min_value > dist[nx][ny]:
                min_value = dist[nx][ny]
                min_x, min_y = nx, ny

        people_pos[i] = (min_x, min_y)

    
    for i in range(m):
        if people_pos[i] == store[i]:
            check_x, check_y = people_pos[i]
            check_visited[check_x][check_y] = True
    
    if time > m :
        return
    
    dist, visited = bfs(store[time - 1][0], store[time - 1][1])
    min_value = 1e9
    min_x, min_y = -1, -1
    for x in range(n):
        for y in range(n):
            if visited[x][y] == True and graph[x][y] == 1 and min_value > dist[x][y]:
                min_value = dist[x][y]
                min_x, min_y = x, y
    people_pos[time - 1] = (min_x, min_y)
    check_visited[min_x][min_y] = True
while True:
    time += 1
    simulate()
    if check():
        break

    
print(time)