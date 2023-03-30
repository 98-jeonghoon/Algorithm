from collections import deque
w, h = map(int, input().split())

graph = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(1, h + 1):
    graph[i][1: w + 1] = map(int, input().split())

# x 가 짝수이면 왼쪽위 왼쪽 아래 (상 하 좌 우는 동일)
# x 가 홀수면 오른쪽위 오른쪽 아래 (상 하 좌 우는 동일)

dx = [-1, 1, 0, 0, -1, 1]
dy = [[0, 0, -1, 1, -1, -1],[0, 0, -1, 1, 1, 1]]

def bfs(x, y):
    queue = deque()
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    queue.append((x, y))
    visited[x][y] = True
    count = 0
    while queue:
        x, y = queue.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[x % 2][d]
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if graph[nx][ny] == 1:
                    count += 1
                elif graph[nx][ny] == 0 and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return count


print(bfs(0, 0))