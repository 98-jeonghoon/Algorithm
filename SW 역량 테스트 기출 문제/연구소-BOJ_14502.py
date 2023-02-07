from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 1:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))
    global result
    cnt = 0
    
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    result = max(result, cnt)

result = 0
def backtracking(depth):
    if depth == 3:
        bfs()
        return
                    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                visited[i][j] = True
                backtracking(depth + 1)
                visited[i][j] = False
                graph[i][j] = 0
                
backtracking(0)
print(result)