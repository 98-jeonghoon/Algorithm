n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int ,input().split())
    graph[a-1][b-1] = 1

l = int(input())
dic = dict()
for _ in range(l):
    sec, dir = input().split()
    dic[int(sec)] = dir

from collections import deque

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dir_change(direction, turn):
    if turn == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def start():
    direction = 1
    time = 1
    x, y = 0, 0
    queue = deque([[y, x]])
    graph[y][x] = 2
    while True:
        y = y + dy[direction]
        x = x + dx[direction]
        if 0 <= y < n and 0 <= x < n and graph[y][x] != 2:
            if not graph[y][x] == 1:
                tmp_y, tmp_x = queue.popleft()
                graph[tmp_y][tmp_x] = 0
            graph[y][x] = 2
            queue.append([y,x])
            if time in dic.keys():
                direction = dir_change(direction, dic[time])
            time += 1
        else:
            return print(time)
        
start()