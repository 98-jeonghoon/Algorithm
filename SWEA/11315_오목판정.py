# 좌하, 하, 우하, 우
dx = [1, 1, 1, 0]
dy = [-1, 0, 1, 1]
def check(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'o':
                for d in range(4):
                    x, y = i, j
                    cnt = 0
                    while 0 <= x < n and 0 <= y < n and graph[x][y] == 'o':
                        cnt += 1
                        x += dx[d]
                        y += dy[d]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'
                    
t = int(input())
for test in range(1, t + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    answer = check(graph)
    print('#{} {}'.format(test, answer))