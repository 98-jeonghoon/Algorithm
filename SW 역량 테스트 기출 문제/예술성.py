from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    group[nx][ny] = group_num
                    group_cnt[group_num] += 1

def score():
    count = 0
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if group[nx][ny] != group[i][j]:
                        g_x, g_y = group[i][j], group[nx][ny]
                        g_x_num, g_y_num = graph[i][j], graph[nx][ny]
                        g_x_count, g_y_count =group_cnt[g_x], group_cnt[g_y]
                        count += (g_x_count + g_y_count) * g_x_num * g_y_num
    return count // 2

def rotate_square(sx, sy, square_n, new_graph):
    for x in range(sx, sx + square_n):
        for y in range(sy, sy + square_n):
            ox, oy = x - sx, y - sy
            rx, ry = oy, square_n - ox - 1
            new_graph[rx + sx][ry + sy] = graph[x][y]

def rotate(graph):
    import copy
    x, y = n // 2, n // 2
    tmp_graph = copy.deepcopy(graph)
    tmp_graph = list(map(list, zip(*tmp_graph)))[::-1]
    graph[x] = tmp_graph[x]
    for i in range(n):
        graph[i][y] = tmp_graph[i][y]
    
    square_n = n // 2
    new_graph = [[0] * n for _ in range(n)]
    rotate_square(0, 0, square_n, new_graph)
    rotate_square(0, square_n + 1, square_n, new_graph)
    rotate_square(square_n + 1, 0, square_n, new_graph)
    rotate_square(square_n + 1, square_n + 1, square_n, new_graph)
    
    for x in range(n):
        for y in range(n):
            if x == square_n or y == square_n:
                continue
            graph[x][y] = new_graph[x][y]

answer = 0

for _ in range(4):
    group = [[0] * n for _ in range(n)]
    group_cnt = [0] * (n * n + 1)
    group_num = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                group_num += 1
                group[i][j] = group_num
                group_cnt[group_num] += 1
                bfs(i,j)

    answer += score()
    rotate(graph)

print(answer)