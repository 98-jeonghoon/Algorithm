from collections import deque
import queue

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()
    
count = 0
visited = [False] * (n+1)

def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)
            
def bfs(graph, v, visited):
    global count
    queue = deque([v])
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = True
                
# dfs(graph, 1, visited)
bfs(graph, 1, visited)
print(count)