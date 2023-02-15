n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * (n + 1)

answer = 1e9
def backtracking(depth, idx):
    global answer
    if depth == (n // 2):
        start, link = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    start += (graph[i][j] + graph[j][i])
                elif not visited[i] and not visited[j]:
                    link += (graph[i][j] + graph[j][i])
        answer = min(answer, abs(start - link))
        return
                
    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = True
        backtracking(depth + 1, i + 1)
        visited[i] = False
        
backtracking(0, 0)
print(answer)