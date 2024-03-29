# 백준 2636 치즈 풀이

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


# 디버깅을 위해 그래프 출력 함수
def PRINT_GRAPH():
    for i in graph:
        print(i)

# PRINT_GRAPH()

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cheese = []
# 빈칸을 기준으로 bfs 탐색을 진행한다
def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                else:
                    graph[nx][ny] = 0
                    visited[nx][ny] = True
                    cnt += 1
    cheese.append(cnt)
    return cnt

time = 0
while True:
    cnt = bfs(0, 0)
    if not cnt:
        break
    time += 1
print(time)
print(cheese[-2])