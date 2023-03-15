from collections import deque
import copy

r, c, k = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(r)]
air = [[0] * c for _ in range(r)]
w = int(input())
wall_hor = [[False] * c for _ in range(r)]
wall_ver = [[False] * c for _ in range(r)]
    
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall_hor[x][y] = True
    elif t == 1:
        wall_ver[x][y] = True
        
def up_ok(x, y, direction):
    if wall_hor[x][y] == True:
        return False
    if not (0 <= x + dx[direction] < r and 0 <= y + dy[direction] < c):
        return False
    return True

def left_ok(x, y, direction):
    if 0 <= x + dx[direction] < r and 0 <= y + dy[direction] < c:
        if wall_ver[x + dx[direction]][y + dy[direction]] == False:
            return True
    return False

def down_ok(x, y, direction):
    if 0 <= x + dx[direction] < r and 0 <= y + dy[direction] < c:
        if wall_hor[x + dx[direction]][y + dy[direction]] == False:
            return True
    return False

def right_ok(x, y, direction):
    if wall_ver[x][y] == True:
        return False
    if not (0 <= x + dx[direction] < r and 0 <= y + dy[direction] < c):
        return False
    return True

def move_air():
    air_position = []
    for x in range(r):
        for y in range(c):
            if 1 <= pan[x][y] <= 4:
                air_position.append((x, y, pan[x][y]))
                
    for x, y, d in air_position:
        tmp = [[0] * c for _ in range(r)]
        x, y = x + dx[d], y + dy[d]
        tmp[x][y] = 5
        
        queue = deque()
        queue.append((x, y, 5))
        
        while queue:
            nx, ny, temper = queue.popleft()
            
            if temper == 0:
                break
            
            if d == 1:
                if up_ok(nx, ny, 3):
                    if right_ok(nx - 1, ny, 1):
                        queue.append((nx - 1, ny + 1, temper - 1))
                        tmp[nx - 1][ny + 1] = temper - 1
                if right_ok(nx, ny, 1):
                    queue.append((nx, ny + 1, temper - 1))
                    tmp[nx][ny + 1] = temper - 1
                if down_ok(nx, ny, 4):
                    if right_ok(nx + 1, ny, 1):
                        queue.append((nx + 1, ny + 1, temper - 1))
                        tmp[nx + 1][ny + 1] = temper - 1
            
            elif d == 2:
                if up_ok(nx, ny, 3):
                    if left_ok(nx - 1, ny, 2):
                        queue.append((nx - 1, ny - 1, temper - 1))
                        tmp[nx - 1][ny - 1] = temper - 1
                if left_ok(nx, ny, 2):
                    queue.append((nx, ny - 1, temper - 1))
                    tmp[nx][ny - 1] = temper - 1
                if down_ok(nx, ny, 4):
                    if left_ok(nx + 1, ny, 2):
                        queue.append((nx + 1, ny - 1, temper - 1))
                        tmp[nx + 1][ny - 1] = temper - 1
            
            elif d == 3:
                if left_ok(nx, ny, 2):
                    if up_ok(nx, ny - 1, 3):
                        queue.append((nx - 1, ny - 1, temper - 1))
                        tmp[nx - 1][ny - 1] = temper - 1
                if up_ok(nx, ny, 3):
                    queue.append((nx - 1, ny, temper - 1))
                    tmp[nx - 1][ny] = temper - 1
                if right_ok(nx, ny, 1):
                    if up_ok(nx, ny + 1, 3):
                        queue.append((nx - 1, ny + 1, temper - 1))
                        tmp[nx - 1][ny + 1] = temper - 1
                        
            elif d == 4:
                if left_ok(nx, ny, 2):
                    if down_ok(nx, ny - 1, 4):
                        queue.append((nx + 1, ny - 1, temper - 1))
                        tmp[nx + 1][ny -1] = temper - 1
                if down_ok(nx, ny, 4):
                    queue.append((nx + 1, ny, temper - 1))
                    tmp[nx + 1][ny] = temper - 1
                if right_ok(nx, ny, 1):
                    if down_ok(nx, ny + 1, 4):
                        queue.append((nx + 1, ny + 1, temper - 1))
                        tmp[nx + 1][ny + 1] = temper - 1
                        
        for x in range(r):
            for y in range(c):
                air[x][y] += tmp[x][y]
            
def tem_adjust():
    tmp = copy.deepcopy(air)
    
    for x in range(r):
        for y in range(c):
            if right_ok(x, y, 1):
                nx = x + dx[1]
                ny = y + dy[1]      
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff
            
            if left_ok(x, y, 2):
                nx = x + dx[2]
                ny = y + dy[2]      
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff      
                    
            if up_ok(x, y, 3):
                nx = x + dx[3]
                ny = y + dy[3]      
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff 
                    
            if down_ok(x, y, 4):
                nx = x + dx[4]
                ny = y + dy[4]      
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff
                    
    return tmp

def decrease():
    for y in range(c):
        if air[0][y] > 0:
            air[0][y] -= 1
    for y in range(c):
        if air[-1][y] > 0:
            air[r - 1][y] -= 1
    
    for x in range(1, r - 1):
        if air[x][0] > 0:
            air[x][0] -= 1
        if air[x][-1] > 0:
            air[x][-1] -= 1
        
def search():
    for x in range(r):
        for y in range(c):
            if pan[x][y] == 5:
                if air[x][y] < k:
                    return False
    return True

answer = 0

while True:
    move_air()
    air = tem_adjust()
    decrease()
    answer += 1
    if search():
        print(answer)
        break
    if answer > 100:
        answer = 101
        print(answer)
        break
    
