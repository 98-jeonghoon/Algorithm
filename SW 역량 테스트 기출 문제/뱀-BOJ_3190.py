n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a- 1][b - 1] = 1

l = int(input())
move = []
for _ in range(l):
    sec, direct = input().split()
    move.append((int(sec), direct))

# 우측부터 시작
#우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

from collections import deque

time = 0
d, check = 0, 0
x, y = 0, 0
queue = deque()
queue.append((x, y))
while True:
    time += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) in queue:
        break
    queue.append((nx, ny))
    if graph[nx][ny] == 0:
        queue.popleft()
    else:
        graph[nx][ny] = 0

    if time == move[check][0]:
        if move[check][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        if check + 1 < len(move):
            check += 1
    x, y = nx, ny
print(time)