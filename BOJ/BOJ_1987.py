r, c = map(int, input().split())
graph = [list(map(lambda a : ord(a)-65,input())) for _ in range(r)]

visited = [0] * 26
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_num = 1
def dfs(x, y, count):
    global max_num
    if max_num < count:
        max_num = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if visited[graph[nx][ny]] == 0:
                visited[graph[nx][ny]] = 1
                dfs(nx, ny, count+1)
                visited[graph[nx][ny]] = 0
                
visited[graph[0][0]] = 1
dfs(0,0, max_num)
print(max_num)