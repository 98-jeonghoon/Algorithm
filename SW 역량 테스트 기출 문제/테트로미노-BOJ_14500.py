n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_num = -1e9

def dfs(x, y, cnt, tmp):
       global max_num
       if cnt == 4:
              max_num = max(max_num, tmp)
              return
       
       for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                     visited[nx][ny] = True
                     dfs(nx, ny,cnt + 1 ,tmp + graph[nx][ny])
                     visited[nx][ny] = False
              
def pink(x, y):
       global max_num
       for i in range(4):
              tmp = graph[x][y]
              for j in range(3):
                     direction = (i + j) % 4
                     nx = x + dx[direction]
                     ny = y + dy[direction]
                     if not (0 <= nx < n and 0 <= ny < m):
                            tmp = 0
                            break
                     tmp += graph[nx][ny]
              max_num = max(max_num, tmp)
                            
                     
for i in range(n):
       for j in range(m):
              visited[i][j] = True
              dfs(i, j, 1, graph[i][j])
              visited[i][j] = False
              pink(i, j)

print(max_num)