n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 토네이도 방향 - 좌 하 우 상
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

x, y = n // 2, n //2
answer = 0

def count(dist, dx, dy, direct):
    global answer, x, y
    for _ in range(dist):
        x += dx
        y += dy
        if y < 0:
            break
        total = 0
        for dx, dy, z in direct:
            nx = x + dx
            ny = y + dy
            if z == 0:
                new_sand = graph[x][y] - total
            else:
                new_sand = int(graph[x][y] * z)
                total += new_sand
            if 0 <= nx < n and 0 <= ny < n:
                graph[nx][ny] += new_sand
            else:
                answer += new_sand

for i in range(1, n + 1):
    if i % 2 == 1:
        count(i, 0, -1, left)
        count(i, 1, 0, down)
    else:
        count(i, 0, 1, right)
        count(i, -1, 0, up)
    
print(answer)

# 나선형 알고리즘
# def init_grid(n):
#     x, y = n // 2, n // 2
#     d, move_count = 0, 0
#     dist = 1
#     n = 0
#     while True:
#         move_count += 1
#         for _ in range(dist):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if (nx, ny) == (0, -1):
#                 return
#             n += 1
#             graph[nx][ny] = n
#             x, y = nx, ny
#         if move_count == 2:
#             dist += 1
#             move_count = 0
#         d = (d + 1) % 4
        
