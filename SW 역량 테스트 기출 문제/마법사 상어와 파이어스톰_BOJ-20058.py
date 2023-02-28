n, q = map(int, input().split())
n = 2 ** n

graph = [list(map(int, input().split())) for _ in range(n)]


l_arr = list(map(int, input().split()))
    
# 우 하 좌 상 -> 시계방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]

def rotate_graph(graph, l):
    l = 2 ** l
    tmp_graph = [[0]* n for _ in range(n)]
    
    for x in range(0, n, l):
        for y in range(0, n, l):
            for i in range(l):
                for j in range(l):
                    tmp_graph[x + i][y + j] = graph[x + l - 1 - j][y + i]
    return tmp_graph

def check_ice(graph):
    tmp_graph = [[0] * n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0:
                        count += 1
            if count < 3 and graph[x][y] != 0:
                tmp_graph[x][y] = graph[x][y] - 1
            else:
                tmp_graph[x][y] = graph[x][y]
                
    return tmp_graph

for i in range(len(l_arr)):
    graph = rotate_graph(graph, l_arr.pop(0))
    graph = check_ice(graph)
    
from collections import deque

def bfs():
    visited = [[False] * n for _ in range(n)]
    sum_ice = 0
    max_area = -1e9
    for i in range(n):
        for j in range(n):
            area = 0
            if visited[i][j] == True or graph[i][j] == 0:
                continue
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            
            while queue:
                x, y = queue.popleft()
                sum_ice += graph[x][y]
                area += 1
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                        continue
                    if graph[nx][ny] != 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            max_area = max(area, max_area)
            
    return [sum_ice, max_area]

for i in bfs():
    print(i)