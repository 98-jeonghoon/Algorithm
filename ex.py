# n, m = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1 , y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# count = 0 

# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             count += 1
            
# print(count)

from collections import deque
            
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n - 1][m - 1]

print(bfs(0, 0))