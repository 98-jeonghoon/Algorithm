n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []
visited = [[False] * n for _ in range(n)]
arr = []
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i,j))
            
def calc():
    tmp = 0
    for r2, c2 in house:
        distance = 1e9
        for e, (r1, c1) in arr:
            distance = min(distance, abs(r1 - r2) + abs(c1 - c2))
        tmp += distance
    res.append(tmp)
def backtracking(cnt):
    if cnt == m:
        calc()
        return
    
    for idx, (r1, c1) in enumerate(chicken):
        if visited[r1][c1] == False:
            if arr:
                if idx < arr[-1][0]:
                    continue
            visited[r1][c1] = True
            arr.append((idx, (r1, c1)))
            backtracking(cnt + 1)
            visited[r1][c1] = False
            arr.pop()
            
            
backtracking(0)
print(min(res))