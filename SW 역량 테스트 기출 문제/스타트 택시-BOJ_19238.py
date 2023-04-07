from collections import deque

n, m, remain = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

x, y = map(int, input().split())
taxi = (x - 1, y - 1)

start = []
end = []
for _ in range(m):
    start_x, start_y, end_x, end_y = map(int, input().split())
    start.append((start_x - 1, start_y - 1))
    end.append((end_x - 1, end_y - 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 최단거리 손님 찾기
def find_passenger(x, y):
    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    min_dist = 1e9
    arr = []
    while queue:
        x, y = queue.popleft()
        if dist[x][y] > min_dist:
            break
        if (x, y) in start:
            min_dist = dist[x][y]
            arr.append((x, y))
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if in_range(nx, ny) and visited[nx][ny] == False and graph[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    if arr:
        arr.sort()
        return dist[arr[0][0]][arr[0][1]], arr[0][0], arr[0][1]
    else:
        return -1, -1, -1

def go_to_destination(start, end):
    dist = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if in_range(nx, ny) and visited[nx][ny] == False and graph[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return dist[x][y], x, y
    # for i in dist:
    #     print(i)

for _ in range(m):
    distance, x, y = find_passenger(taxi[0], taxi[1])
    if distance == -1 or remain - distance < 0:
        remain = -1
        break
    remain -= distance
    idx = start.index((x, y))
    # print(distance, x, y)
    # print(idx)
    start[idx] = (-1, -1)
    distance2, x2, y2 = go_to_destination((x, y), end[idx])
    if (x2, y2) != end[idx] or remain - distance2 < 0:
        remain = -1
        break
    remain += distance2
    taxi = (x2, y2)

print(remain)