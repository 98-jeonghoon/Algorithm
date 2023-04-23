n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
side_dx = [-1, -1, 1, 1]
side_dy = [-1, 1, -1, 1]
herb = [[0] * n for _ in range(n)]

# def grow():
#     tmp_graph = [[0] * n for _ in range(n)]            
#     for x in range(n):
#         for y in range(n):
#             if graph[x][y] >= 1:
#                 check, check_arr, around = 0, [], 0
#                 for d in range(4):
#                     nx = x + dx[d]
#                     ny = y + dy[d]
#                     if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and herb[nx][ny] == 0:
#                         check += 1
#                         check_arr.append((nx, ny))
#                     if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] >= 1 and herb[nx][ny] == 0:
#                         around += 1
#                 graph[x][y] += around
#                 if check == 0:
#                     tree = 0
#                 else:
#                     tree = graph[x][y] // check
#                 for tmp_x, tmp_y in check_arr:
#                     tmp_graph[tmp_x][tmp_y] += tree
#                 check_arr.clear()
#     for x in range(n):
#         for y in range(n):
#             graph[x][y] += tmp_graph[x][y]

def step_one():
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 1:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                        cnt += 1

                graph[x][y] += cnt

def step_two():
    tmp_graph = [[0] * n for _ in range(n)]  
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 1: 
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and herb[nx][ny] == 0:
                        if graph[nx][ny] == 0: 
                            cnt += 1

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and herb[nx][ny] == 0:
                        if graph[nx][ny] == 0:
                            tmp_graph[nx][ny] += graph[x][y] // cnt
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp_graph[i][j]


answer = 0
def find():
    global answer
    max_count = -1e9
    max_x, max_y = -1, -1
    
    for x in range(n):
        for y in range(n):
            if graph[x][y] <= 0:
                continue
            cnt = graph[x][y]
            for d in range(4):
                nx, ny = x, y
                for _ in range(k):
                    nx += side_dx[d]
                    ny += side_dy[d]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        break
                    if graph[nx][ny] <= 0:
                        break
                    cnt += graph[nx][ny]
            if max_count < cnt:
                max_count = cnt
                max_x, max_y = x, y
    answer += max_count
    
    if graph[max_x][max_y] > 0:
        graph[max_x][max_y] = 0
        herb[max_x][max_y] = 0
        
        for d in range(4):
            nx, ny = max_x, max_y
            for _ in range(k):
                nx += side_dx[d]
                ny += side_dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                if graph[nx][ny] < 0:
                    break
                if graph[nx][ny] == 0:
                    herb[nx][ny] = c
                    break
                
                graph[nx][ny] = 0
                herb[nx][ny] = c
                
    

def delete_herb():
    for i in range(n):
        for j in range(n): 
            if herb[i][j] > 0: 
                herb[i][j] -= 1
                
for _ in range(m):
    step_one()
    step_two()
    delete_herb()
    find()

print(answer)