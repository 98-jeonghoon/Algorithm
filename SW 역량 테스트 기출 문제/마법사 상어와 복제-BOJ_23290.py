import copy

graph = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
m, s = map(int, input().split())

for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x-1][y-1].append(d-1)
    
x, y = map(int, input().split())
shark = (x - 1, y - 1)

fish_dx = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dy = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

def move_fish():
    fish_graph = [[[] for _ in range(4)] for _ in range(4)]
    
    for x in range(4):
        for y in range(4):
            while temp_graph[x][y]:
                d = temp_graph[x][y].pop()
                for i in range(d, d-8, -1):
                    i = i % 8
                    nx = x + fish_dx[i]
                    ny = y + fish_dy[i]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        fish_graph[nx][ny].append(i)
                        break
                else:
                    fish_graph[x][y].append(d)
    return fish_graph

def dfs(x, y, depth, cnt, visited):
    global max_eat, shark, eat
    if depth == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visited[:]
        return
    
    for i in range(4):
        nx = x + shark_dx[i]
        ny = y + shark_dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                dfs(nx, ny, depth + 1, cnt + len(temp_graph[nx][ny]), visited)
                visited.pop()
            else:
                dfs(nx, ny, depth + 1, cnt, visited)
        
    
            
            
for _ in range(s):
    eat = []
    max_eat = -1e9
    temp_graph = copy.deepcopy(graph)
    temp_graph = move_fish()
    
    shark_x, shark_y = shark[0], shark[1]
    dfs(shark_x, shark_y, 0, 0, [])
    
    for x, y in eat:
        if temp_graph[x][y]:
            temp_graph[x][y] = []
            smell[x][y] = 3
            
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
                
    for i in range(4):
        for j in range(4):
            graph[i][j] += temp_graph[i][j]
            
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(graph[i][j])
        
print(answer)

