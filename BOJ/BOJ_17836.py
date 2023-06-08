from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. 처음부터 끝까지 가는 경우의 수
# 2. 검을 먼저 잡고 벽을 뚫고 가는 경우의 수
# 3. 검을 잡을 수도 없고, 벽에 막혀서 도착할 수 없는 경우의 수

sword = 1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global sword
    dist = [[-1] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dist[x][y] = 0
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 만약 칼을 만났다면
        if graph[x][y] == 2:
            # 해당 칼까지 온 위치 + 칼에서 n - 1, m - 1 까지의 위치
            sword = dist[x][y] + (n - 1 - x) + (m - 1 - y)
        
        # 만약 x, y가 끝단까지 도착했다면
        if (x == n - 1) and (y == m - 1):
            return min(sword, dist[x][y])
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] != 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    # 만약 끝단까지 못갔다면 sword 거리를 리턴
    return sword

answer = bfs(0, 0)
if answer > t:
    print('Fail')
else:
    print(answer)
