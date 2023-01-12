n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and l <= (abs(graph[nx][ny] - graph[x][y])) <= r:
                arr.append((nx, ny))
                dfs(nx, ny)
    return arr
answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            arr = [(i, j)]
            if not visited[i][j]:
                arr = dfs(i,j)
            if len(arr) > 1:
                flag = True
                sum = 0
                for x, y in arr:
                    sum += graph[x][y]
                avg = sum // len(arr)
                for a, b in arr:
                    graph[a][b] = int(avg)
    if not flag:
        print(answer)
        break
    answer += 1