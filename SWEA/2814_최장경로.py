def dfs(start, cnt):
    global answer
    if cnt > answer:
        answer = cnt
    for now in graph[start]:
        if not visited[now]:
            visited[now] = True
            dfs(now, cnt + 1)
            visited[now] = False

t = int(input())
for test in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    answer = 0
    for i in range(1, n + 1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    print(f'#{test} {answer}')
    