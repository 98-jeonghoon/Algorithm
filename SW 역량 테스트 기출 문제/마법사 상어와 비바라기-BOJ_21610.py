n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

command = []
for _ in range(m):
    d, s = map(int, input().split())
    command.append((d - 1, s))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
tmp = []
def move_cloud(d, s):
    global cloud
    for _ in range(len(cloud)):
        x, y = cloud.pop(0)
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        cloud.append((nx, ny))
        tmp.append((nx, ny))
    
def rained():
    for i in range(len(cloud)):
        x, y = cloud[i]
        graph[x][y] += 1

def step_3():
    while cloud:
        x, y = cloud.pop()
        count = 0
        for d in [1, 3, 5, 7]:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0:
                    count += 1
        graph[x][y] += count

def append_cloud():
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 2 and (x, y) not in tmp:
                graph[x][y] -= 2
                cloud.append((x, y))
    
    tmp.clear()

for _ in range(m):
    d, s = command.pop(0)
    move_cloud(d, s)
    rained()
    step_3()
    append_cloud()


answer = 0
for i in range(n):
    for j in range(n):
        answer += graph[i][j]

print(answer)