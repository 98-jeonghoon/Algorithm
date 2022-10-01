from collections import deque
import copy
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

red_graph = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            red_graph[i][j] = 'R'
        else:
            red_graph[i][j] = graph[i][j]
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph, color):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == color:
                graph[nx][ny] = '0'
                queue.append((nx, ny))
            
count = 0
red_count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] in 'RGB':
            bfs(i, j, graph, graph[i][j])
            count += 1
            
        if red_graph[i][j] in 'RB':
            bfs(i, j, red_graph, red_graph[i][j])
            red_count += 1
            
print(count , red_count)
