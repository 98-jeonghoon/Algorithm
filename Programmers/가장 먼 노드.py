from collections import deque

def solution(n, edge):
    answer = 0
    visited = [0] * (n + 1)
    visited[1] = 1
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    for i in range(n + 1):
        graph[i].sort()
    print(graph)
    bfs(graph, 1, visited)

    max_edge = max(visited)
    answer = visited.count(max_edge)
    return answer

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[now] + 1



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))