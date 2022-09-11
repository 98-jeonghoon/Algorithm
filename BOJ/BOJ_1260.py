n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()
    
visited = [False] * (n+1)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
dfs(graph, v, visited)
print()

visited = [False] * (n+1)

from collections import deque
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
bfs(graph, v, visited)
        
    