t = int(input())
for test in range(t):
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    num = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    count = n ** 2
    direct = 0
    x, y = 0, 0
    while num <= count:
        graph[x][y] = num
        nx = x + dx[direct]
        ny = y + dy[direct]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] != 0:
            direct = (direct + 1) % 4
            nx = x + dx[direct]
            ny = y + dy[direct]
        x, y = nx, ny
        num += 1
    print('#{}'.format(test + 1))
    for i in graph:
        print(*i)