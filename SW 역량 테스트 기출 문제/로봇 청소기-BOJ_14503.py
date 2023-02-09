n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
graph[r][c] = 2
while True:
    flag = 0
    for i in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                count += 1
                r, c = nx, ny
                flag = 1
                break
        
    if flag == 0:
        if graph[r - dx[d]][c - dy[d]] == 1:
            print(count)
            break
        else:
            r, c = r - dx[d], c - dy[d]