n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            red_x, red_y = i, j
        elif graph[i][j] == 'B':
            blue_x, blue_y = i, j
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    count = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

from collections import deque

def bfs(red_x, red_y, blue_x, blue_y, depth):
    queue = deque()
    queue.append((red_x, red_y, blue_x, blue_y, depth))
    visited = []
    visited.append((red_x, red_y, blue_x, blue_y))
    while queue:
        red_x, red_y, blue_x, blue_y, depth = queue.popleft()
        if depth > 10:
            break
        for i in range(4):
            nx_red, ny_red, red_count = move(red_x, red_y, dx[i], dy[i])
            nx_blue, ny_blue, blue_count = move(blue_x, blue_y, dx[i], dy[i])
            
            if graph[nx_blue][ny_blue] == 'O':
                continue
            if graph[nx_red][ny_red] == 'O':
                print(depth)
                return
            if nx_red == nx_blue and ny_red == ny_blue:
                if red_count > blue_count:
                    nx_red -= dx[i]
                    ny_red -= dy[i]
                else:
                    nx_blue -= dx[i]
                    ny_blue -= dy[i]
            if (nx_red, ny_red, nx_blue, ny_blue) not in visited:
                queue.append((nx_red, ny_red, nx_blue, ny_blue, depth + 1))
                visited.append((nx_red, ny_red, nx_blue, ny_blue))
    print(-1)
    
bfs(red_x, red_y, blue_x, blue_y, 1)

 