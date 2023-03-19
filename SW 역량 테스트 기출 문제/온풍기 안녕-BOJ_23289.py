from collections import deque
import copy

n, m, k = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(n)]
air = [[0] * m for _ in range(n)]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

w = int(input())
wall_height = [[False] * m for _ in range(n)]
wall_width = [[False] * m for _ in range(n)]

for _ in range(w):
    x, y, t = map(int, input().split())
    if t == 0:
        wall_height[x - 1][y - 1] = True
    elif t == 1:
        wall_width[x - 1][y - 1] = True


def up_possible(x, y, direction):
    if wall_height[x][y] == True:
        return False
    if not (0 <= x + dx[direction] < n and 0 <= y + dy[direction] < m):
        return False
    return True

def down_possible(x, y, direction):
    if 0 <= x + dx[direction] < n and 0 <= y + dy[direction] < m:
        if wall_height[x + dx[direction]][y + dy[direction]] == False:
            return True
    return False

def right_possible(x, y, direction):
    if wall_width[x][y] == True:
        return False
    if not (0 <= x + dx[direction] < n and 0 <= y + dy[direction] < m):
        return False
    return True

def left_possible(x, y, direction):
    if 0 <= x + dx[direction] < n and 0 <= y + dy[direction] < m:
        if wall_width[x + dx[direction]][y + dy[direction]] == False:
            return True
    return False

def pan_on():
    position = []
    for x in range(n):
        for y in range(m):
            if 1 <= pan[x][y] <= 4:
                position.append((x, y, pan[x][y]))
    
    for x, y, d in position:
        tmp = [[0] * m for _ in range(n)]
        x = x + dx[d]
        y = y + dy[d]
        tmp[x][y] = 5
        
        queue = deque()
        queue.append((x, y, 5))
        
        while queue:
            nx, ny, temper = queue.popleft()
            
            if temper == 0:
                break
            
            # 방향 -> 위쪽 = 3 / 오른쪽 = 1 / 왼쪽 = 2 / 아래쪽 = 4
            # 방향이 오른쪽인 온풍기면 -> 위, 오른쪽 / 오른쪽 / 아래쪽, 오른쪽 -> 이렇게 퍼짐
            if d == 1:
                # 위 , 오른쪽
                if up_possible(nx, ny, 3):
                    if right_possible(nx - 1, ny, 1):
                        queue.append((nx - 1, ny + 1, temper - 1))
                        tmp[nx - 1][ny + 1] = temper - 1
                # 오른쪽
                if right_possible(nx, ny, 1):
                    queue.append((nx, ny + 1, temper - 1))
                    tmp[nx][ny + 1] = temper - 1
                # 아래쪽, 오른쪽
                if down_possible(nx, ny, 4):
                    if right_possible(nx + 1, ny, 1):
                        queue.append((nx + 1, ny + 1, temper - 1))
                        tmp[nx + 1][ny + 1] = temper - 1
            
            # 방향이 왼쪽인 온풍기는 -> 위, 왼쪽 / 왼쪽 / 아래, 왼쪽
            elif d == 2:
                # 위, 왼쪽
                if up_possible(nx, ny, 3):
                    if left_possible(nx - 1, ny, 2):
                        queue.append((nx - 1, ny - 1, temper - 1))
                        tmp[nx - 1][ny - 1] = temper - 1
                # 왼쪽
                if left_possible(nx, ny, 2):
                    queue.append((nx, ny - 1, temper - 1))
                    tmp[nx][ny - 1] = temper - 1
                
                # 아래, 왼쪽
                if down_possible(nx, ny, 4):
                    if left_possible(nx + 1, ny, 2):
                        queue.append((nx + 1, ny - 1, temper - 1))
                        tmp[nx + 1][ny - 1] = temper - 1
            
            # 방향이 위쪽인 온풍기는 -> 왼, 위쪽 / 위쪽 / 오른, 위쪽
            elif d == 3:
                # 왼, 위쪽
                if left_possible(nx, ny, 2):
                    if up_possible(nx, ny - 1, 3):
                        queue.append((nx - 1, ny - 1, temper - 1))
                        tmp[nx - 1][ny - 1] = temper - 1
                # 위족
                if up_possible(nx, ny, 3):
                    queue.append((nx - 1, ny, temper - 1))
                    tmp[nx - 1][ny] = temper - 1
                # 오른, 위쪽
                if right_possible(nx, ny, 1):
                    if up_possible(nx, ny + 1, 3):
                        queue.append((nx - 1, ny + 1, temper - 1))
                        tmp[nx - 1][ny + 1] = temper - 1
            
            # 방향이 아래쪽인 온풍기는 -> 왼, 아래 / 아래 / 오른, 아래
            elif d == 4:
                # 왼, 아래
                if left_possible(nx, ny, 2):
                    if down_possible(nx, ny - 1, 4):
                        queue.append((nx + 1, ny - 1, temper - 1))
                        tmp[nx + 1][ny - 1] = temper - 1
                # 아래
                if down_possible(nx, ny, 4):
                    queue.append((nx + 1, ny, temper - 1))
                    tmp[nx + 1][ny] = temper - 1
                # 오른, 아래
                if right_possible(nx, ny, 1):
                    if down_possible(nx, ny + 1, 4):
                        queue.append((nx + 1, ny + 1, temper - 1))
                        tmp[nx + 1][ny + 1] = temper - 1
        
        for x in range(n):
            for y in range(m):
                air[x][y] += tmp[x][y]


def control():
    tmp = copy.deepcopy(air)
    
    for x in range(n):
        for y in range(m):
            # up, donw, left, right
            if up_possible(x, y, 3):
                nx = x + dx[3]
                ny = y + dy[3]
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff
                    
            if down_possible(x, y, 4):
                nx = x + dx[4]
                ny = y + dy[4]
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff
                    
            if right_possible(x, y, 1):
                nx = x + dx[1]
                ny = y + dy[1]
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff
                    
            if left_possible(x, y, 2):
                nx = x + dx[2]
                ny = y + dy[2]
                diff = abs(air[x][y] - air[nx][ny]) // 4
                
                if air[x][y] > air[nx][ny]:
                    tmp[x][y] -= diff
                elif air[x][y] < air[nx][ny]:
                    tmp[x][y] += diff
    return tmp

def donw_temper():
    for i in range(len(air[0])):
        if air[0][i] > 0:
            air[0][i] -= 1
    
    for i in range(len(air[0])):
        if air[-1][i] > 0:
            air[-1][i] -= 1

    #여기서 주의 할점이 가로줄에 처리한게 또 처리되면 안됨
    # 따라서 범위를 세로 1번부터 마지막 -1 까지 처리해줘야됨
    
    for i in range(1, len(air) - 1):
        if air[i][0] > 0:
            air[i][0] -= 1
        if air[i][-1] > 0:
            air[i][-1] -= 1
            
def test():
    for x in range(n):
        for y in range(m):
            if pan[x][y] == 5:
                if air[x][y] < k:
                    return False
    return True


chocolate = 0

while True:
    pan_on()
    air = control()
    donw_temper()
    chocolate += 1
    if test():
        print(chocolate)
        break
    if chocolate > 100:
        chocolate = 101
        print(chocolate)
        break
    
