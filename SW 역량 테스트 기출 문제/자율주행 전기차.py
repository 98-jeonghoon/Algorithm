from collections import deque
NOT_EXISTS = (-1, -1)
n, m, remaining_battery = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
step = [[0] * n for _ in range(n)]

x, y = map(int, input().split())
car_pos = (x - 1, y - 1)
passengers = []
for _ in range(m):
    x_s, y_s, x_e, y_e = map(int, input().split())
    passengers.append((x_s - 1, y_s - 1, x_e - 1, y_e - 1))

moved_passenger = [False for _ in range(n * n)]
visitied = [[False] * n for _ in range(n)]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visitied[i][j] = False

def bfs(start_pos):
    initialize_visited()
    start_x, start_y = start_pos
    queue = deque()
    visitied[start_x][start_y] = True
    step[start_x][start_y] = 0    
    queue.append((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if in_range(nx, ny) and visitied[nx][ny] == False and graph[nx][ny] == 0:
                queue.append((nx, ny))
                step[nx][ny] = step[x][y] + 1
                visitied[nx][ny] = True

def need_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True
    
    best_x, best_y = best_pos
    new_x, new_y = new_pos
    
    return (step[best_x][best_y], best_x, best_y) > (step[new_x][new_y], new_x, new_y)
    
def move_passenger():
    global car_pos, remaining_battery
    
    bfs(car_pos)
    
    best_pos, best_index = NOT_EXISTS, -1
    
    for i, (start_x, start_y, end_x, end_y) in enumerate(passengers):
        if moved_passenger[i] or not visitied[start_x][start_y] or step[start_x][start_y] > remaining_battery:
            continue
        if need_update(best_pos, (start_x, start_y)):
            best_pos, best_index = (start_x, start_y), i
    
    if best_pos == NOT_EXISTS:
        return False
    
    start_x, start_y, end_x, end_y = passengers[best_index]
    
    car_pos = (start_x, start_y)
    remaining_battery -= step[start_x][start_y]
    
    bfs((start_x, start_y))
    
    if not visitied[end_x][end_y] or step[end_x][end_y] > remaining_battery:
        return False
    
    car_pos = (end_x, end_y)
    remaining_battery -= step[end_x][end_y]
    
    moved_passenger[best_index] = True
    remaining_battery += step[end_x][end_y] * 2
    
    return True


for _ in range(m):
    is_moved = move_passenger()
    if not is_moved:
        print(-1)
        exit(0)
print(remaining_battery)
print(moved_passenger)