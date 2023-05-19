# t = int(input())
# for test in range(1, t + 1):
#     h, w = map(int, input().split())

#     graph = [list(input()) for _ in range(h)]
#     n = int(input())
#     commands = list(input())
#     tank_pos = (0, 0, 0)

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]


#     def tank_move(x, y, d):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < h and 0 <= ny < w:
#             if graph[nx][ny] == '.':
#                 graph[x][y] = '.'
#                 x, y = nx, ny
#                 if d == 0:
#                     graph[nx][ny] = '^'
#                 elif d == 1:
#                     graph[nx][ny] = 'v'
#                 elif d == 2:
#                     graph[nx][ny] = '<'
#                 elif d == 3:
#                     graph[nx][ny] = '>'
#                 return x, y, d
#             else:
#                 return x, y, d

#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] in ['<', '>', '^', 'v']:
#                 if graph[i][j] == '>':
#                     tank_pos = (i, j, 3)
#                 elif graph[i][j] == '<':
#                     tank_pos = (i, j, 2)
#                 elif graph[i][j] == '^':
#                     tank_pos = (i, j, 0)
#                 else:
#                     tank_pos = (i, j, 1)
#     for command in commands:
#         if command == 'S':
#             x, y, d = tank_pos
#             while True:
#                 x += dx[d]
#                 y += dy[d]
#                 if 0 <= x < h and 0 <= y < w:
#                     if graph[x][y] == '.':
#                         continue
#                     elif graph[x][y] == '*':
#                         graph[x][y] = '.'
#                         break
#                     elif graph[x][y] == '#':
#                         break
#                 else:
#                     break
#         else:
#             # 상 하 좌 우 순서임
#             if command == 'U':
#                 x, y, d = tank_pos[0], tank_pos[1], 0
#                 tank_pos = tank_move(x, y, d)
#             elif command == 'D':
#                 x, y, d = tank_pos[0], tank_pos[1], 1
#                 tank_pos = tank_move(x, y, d)
#             elif command == 'L':
#                 x, y, d = tank_pos[0], tank_pos[1], 2
#                 tank_pos = tank_move(x, y, d)
#             else:
#                 x, y, d = tank_pos[0], tank_pos[1], 3
#                 tank_pos = tank_move(x, y, d)
        
#     print(f'#{test}')
#     for i in graph:
#         print(''.join(i))

def tank_move(x, y, d):
    graph[x][y] = '.'
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < h and 0 <= ny < w:
        if graph[nx][ny] == '.':
            x, y = nx, ny
    graph[x][y] = ['^', 'v', '<', '>'][d]
    return x, y, d

t = int(input())
for test in range(1, t + 1):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    n = int(input())
    commands = list(input())
    tank_pos = (0, 0, 0)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(h):
        for j in range(w):
            if graph[i][j] in ['<', '>', '^', 'v']:
                tank_pos = (i, j, ['^', 'v', '<', '>'].index(graph[i][j]))

    for command in commands:
        if command == 'S':
            x, y, d = tank_pos
            while True:
                x += dx[d]
                y += dy[d]
                if 0 <= x < h and 0 <= y < w:
                    if graph[x][y] == '.':
                        continue
                    elif graph[x][y] == '*':
                        graph[x][y] = '.'
                        break
                    elif graph[x][y] == '#':
                        break
                else:
                    break
        else:
            d = {'U': 0, 'D': 1, 'L': 2, 'R': 3}[command]
            tank_pos = tank_move(tank_pos[0], tank_pos[1], d)

    print(f'#{test} ',end='')
    for i in graph:
        print(''.join(i))
