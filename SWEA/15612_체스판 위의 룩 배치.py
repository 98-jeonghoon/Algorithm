t = int(input())
for test in range(t):
    graph = [list(input()) for _ in range(8)]
    rook_count = 0
    pos = []
    for i in range(8):
        for j in range(8):
            if graph[i][j] == 'O':
                pos.append((i, j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def check(x, y, direct):
        # 위쪽 확인
        while True:
            nx = x + dx[direct]
            ny = y + dy[direct]
            if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
                break
            if graph[nx][ny] == 'O':
                return False
            x, y = nx, ny
        return True
        
    answer = ''
    if len(pos) == 8:
        for x, y in pos:
            flag = True
            for d in range(4):
                if not check(x, y, d):
                    flag = False
            if flag == False:
                answer = 'no'
                break
        else:
            answer = 'yes'
    else:
        answer = 'no'

    print('#{} {}'.format(test + 1, answer))