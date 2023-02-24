N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
fire_ball = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_ball.append([r-1, c-1, m, s, d])
    
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fire_ball:
        r, c, m, s, d = fire_ball.pop(0)
        nr = (r + s * dx[d]) % N
        nc = (c + s * dy[d]) % N
        graph[nr][nc].append([m, s, d])
    
    for r in range(N):
        for c in range(N):
            if len(graph[r][c]) >= 2:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[r][c])
                while graph[r][c]:
                    m, s, d = graph[r][c].pop(0)
                    sum_m += m
                    sum_s += s
                    if d % 2 == 1:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:
                    for d in nd:
                        fire_ball.append([r, c, sum_m // 5, sum_s // cnt, d])
            if len(graph[r][c]) == 1:
                fire_ball.append([r, c] + graph[r][c].pop())
                
answer = 0
for i in fire_ball:
    answer += i[2]
    
print(answer)