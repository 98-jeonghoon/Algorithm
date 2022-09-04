from collections import deque

n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()
    

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for j in graph[now]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                
visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)


