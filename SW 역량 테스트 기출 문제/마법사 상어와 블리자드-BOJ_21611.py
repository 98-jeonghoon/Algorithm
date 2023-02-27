n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
init_graph = []
shark_set = []
for _ in range(m):
    d, s = map(int, input().split())
    shark_set.append((d , s))
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def init_grid(n):
    x, y = n // 2, n // 2
    tornado_dx = [0, 1, 0, -1]
    tornado_dy = [-1, 0, 1, 0]
    direct, move_count= 0, 0
    dist = 1
    while True:
        move_count += 1
        for _ in range(dist):
            nx = x + tornado_dx[direct]
            ny = y + tornado_dy[direct]
            if (nx, ny) == (0, -1):
                return
            init_graph.append(graph[nx][ny])
            x, y = nx, ny
        if move_count == 2:
            dist += 1
            move_count = 0
        direct = (direct + 1) % 4
init_grid(n)
print(len(init_graph))


## 첫번째 시도.
## 실패 -> 2차원 배열를 유지한채로 구현할려고 하니 빈칸을 채우는 과정에서 막힘
## 시간복잡도 O(N^2)로 시간초과 확률이 매우큼

# n, m = map(int,input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# init_graph = [[0] * n for _ in range(n)]

# shark_set = []
# for _ in range(m):
#     d, s = map(int, input().split())
#     shark_set.append((d - 1, s))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def init_grid(n):
#     x, y = n // 2, n // 2
#     tornado_dx = [0, 1, 0, -1]
#     tornado_dy = [-1, 0, 1, 0]
#     direct, move_count, num = 0, 0, 0
#     dist = 1
#     while True:
#         move_count += 1
#         for _ in range(dist):
#             nx = x + tornado_dx[direct]
#             ny = y + tornado_dy[direct]
#             if (nx, ny) == (0, -1):
#                 return
#             num += 1
#             init_graph[nx][ny] = num
#             x, y = nx, ny
#         if move_count == 2:
#             dist += 1
#             move_count = 0
#         direct = (direct + 1) % 4
        
# init_grid(n)

# def destory():
#     d, s = shark_set.pop(0)
    
#     for i in range(n):
#         for j in range(n):
#             if init_graph[i][j] == s + 1:
#                 x, y = i, j
                
#     graph[x][y] = 0
#     while True:
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:
#             break
#         graph[nx][ny] = 0
#         x, y = nx, ny
        
# destory()

# # def explode():
    
# # for i in graph:
# #     print(i)