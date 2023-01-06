N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (N+1)
answer = 1e9

def solve(depth, idx):
    global answer
    if depth == (N // 2): # N // 2 번만큼 재귀를 돌면
        start, link = 0, 0 
        for i in range(N): 
            for j in range(i + 1, N): 
                if visited[i] and visited[j]: 
                    start += (graph[i][j] + graph[j][i]) 
                elif not visited[i] and not visited[j]: 
                    link += (graph[i][j] + graph[j][i])  
        answer = min(answer, abs(start - link))
        return

    #백트래킹하면서 경우의 수 계산하기
    for i in range(idx, N): 
        if visited[i]: 
            continue
        visited[i] = True 
        solve(depth + 1, i + 1) 
        visited[i] = False 



solve(0, 0)
print(answer)