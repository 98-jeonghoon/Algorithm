n, m, h = map(int, input().split())

graph = [[0] *n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    
answer = 4

def check():
    for i in range(n):
        temp = i
        for j in range(h):
            if graph[j][temp]:
                temp += 1
            elif temp > 0 and graph[j][temp - 1]:
                temp -= 1
        if temp != i:
            return False
    return True


def dfs(depth, x, y):
    global answer
    
    if answer <= depth:
        return
    if check():
        answer = min(answer, depth)
    if depth == 3:
        return
    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n - 1):
            if graph[i][j] == 1:
                continue
            graph[i][j] = 1
            dfs(depth + 1, i, j + 2)
            graph[i][j] = 0

dfs(0, 0, 0)
if answer <= 3:
    print(answer)
else:
    print(-1)                