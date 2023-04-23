graph = [list(input()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 블록찾기
def bfs(x, y, color):
    from collections import deque
    queue = deque()
    visited = [[False] * 6 for _ in range(12)]
    visited[x][y] = True
    queue.append((x, y))
    remove.append((x, y))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if graph[nx][ny] == color and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    remove.append((nx, ny))
                    

# 블록 부수기
def remove_block(remove):
    for x, y in remove:
        graph[x][y] = '.'

# 디버깅전용
def print_graph(graph):
    for i in graph:
        print(i)

# 중력작용
def gravity():
    for i in range(11, -1, -1):
        for j in range(6):
            if graph[i][j] != '.':
                tmp = i
                while True:
                    if 0 <= tmp + 1 < 12 and graph[tmp + 1][j] == '.':
                        graph[tmp + 1][j] = graph[tmp][j]
                        graph[tmp][j] = '.'
                        tmp += 1
                    else:
                        break

# 로직
answer = 0
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                remove = []
                bfs(i, j, graph[i][j])
                if len(remove) >= 4:
                    flag = True
                    remove_block(remove)
    
    if flag == False:
        break
    else:
        gravity()
        answer += 1
                    
print(answer)
# for i in graph:
#     print(i)
                
