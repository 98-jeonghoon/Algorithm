n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = -1e9

def dfs(depth, x, y, total):
    global answer
    
    if depth == 4:
        answer = max(answer, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            dfs(depth + 1, nx, ny, total + graph[nx][ny])
            visited[nx][ny] = False
            
def purple(x, y):
    global answer
    for i in range(4):
        tmp = graph[x][y]
        for j in range(3):
            d = (i + j) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                tmp = 0
                break
            else:
                tmp += graph[nx][ny]
        answer = max(answer, tmp)
            

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, i, j, graph[i][j])
        visited[i][j] = False
        purple(i, j)

print(answer)