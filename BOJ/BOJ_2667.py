from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
num = []
#상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                count += 1
                graph[nx][ny]=0
                queue.append((nx, ny))
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            num.append(bfs(i,j))

num.sort()
print(len(num))
for i in range(len(num)):
    print(num[i])

# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
# num = []
# #상 하 좌 우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def dfs(x,y):
#     if x <= -1 or y <= -1 or x >=n or y >=n:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         global count
#         count += 1
#         for i in range(4):
#             nx = x +dx[i]
#             ny = y +dy[i]
#             dfs(nx,ny)
#         return True
#     return False

# count = 0
# result = 0
# for i in range(n):
#     for j in range(n):
#         if dfs(i,j) == True:
#             num.append(count)
#             count = 0
#             result += 1

# num.sort()
# print(result)
# for i in range(len(num)):
#     print(num[i])
