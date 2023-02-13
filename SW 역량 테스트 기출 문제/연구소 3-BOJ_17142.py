from collections import deque
from itertools import combinations


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(comb):
    result = 0
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    
    for x, y in comb:
        visited[x][y] = 0
        queue.append((x, y))
        
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    result = max(result, visited[nx][ny])
                elif visited[nx][ny] == -1 and graph[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    if list(sum(visited, [])).count(-1) != wall_cnt:
        return 1e9
    return result
            
                
arr = []
wall_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            arr.append((i, j))
        elif graph[i][j] == 1:
            wall_cnt += 1
            
answer = 1e9
for comb in combinations(arr, m):
    answer = min(answer, bfs(comb))


if answer == 1e9:
    print(-1)
else:
    print(answer)