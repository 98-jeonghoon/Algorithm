n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# for i in range(n + 1):
#     graph[i].sort()
    
def bfs(start):
    from collections import deque
    queue = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[now] + 1
    return sum(visited)

answer = []

for i in range(1, n + 1):
    answer.append((bfs(i)))

print(answer.index(min(answer)) + 1)