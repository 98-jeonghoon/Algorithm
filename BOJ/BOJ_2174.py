# 가로 세로 주의하기
c, r = map(int, input().split())
# c, r = c - 1, r - 1
n, m = map(int, input().split())
graph = [[None] * c for _ in range(r)]
robot = dict()

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 로봇의 초기 위치 및 방향
for i in range(1, n + 1):
    y, x, d = input().split()
    if d == 'N':
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    else:
        d = 3
    graph[r - int(x)][int(y) - 1] = (i, d)
    robot[i] = (r - int(x), int(y) - 1, d)

commands = []
for _ in range(m):
    q, w, e = input().split()
    commands.append((q, w, e))

for num, command, repeat in commands:
    for _ in range(int(repeat)):
        x, y, d = robot[int(num)]
        if command == 'L':
            d = (d - 1) % 4
            robot[int(num)] = (x, y, d)
        elif command == 'R':
            d = (d + 1) % 4
            robot[int(num)] = (x, y, d)
        else:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= int(r) or ny >= int(c):
                print(f"Robot {num} crashes into the wall")
                exit(0)
            elif graph[nx][ny] != None:
                for i in robot:
                    if nx == robot[i][0] and ny == robot[i][1]:
                        print(f'Robot {num} crashes into robot {i}')
                        exit(0)
            else:
                graph[x][y] = None
                graph[nx][ny] = (num, d)
                robot[int(num)] = (nx, ny, d)
print('OK')

