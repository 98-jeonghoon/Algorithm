from collections import deque
import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def makewall(count):
  if count == 3:
    virus()
    return
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        makewall(count+1)
        graph[i][j] = 0
        
def virus():
  global result
  queue = deque()
  temp_graph = copy.deepcopy(graph)
  for i in range(n):
    for j in range(m):
      if temp_graph[i][j] == 2:
        queue.append((i, j))
        
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if temp_graph[nx][ny] == 0:
        temp_graph[nx][ny] = 2
        queue.append((nx, ny))
  cnt = 0
  
  for i in range(n):
      cnt += temp_graph[i].count(0)
      
  result = max(result, cnt)
  
result = 0
makewall(0)
print(result)