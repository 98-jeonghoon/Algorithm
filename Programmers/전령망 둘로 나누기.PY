from collections import deque   
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count

def solution(n, wires):
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    for start, not_visited in wires:
        visited = [False] * (n + 1)
        visited[not_visited] = True
        count = bfs(graph, start, visited)
        answer = min(answer, abs(count - (n - count)))
    
    return answer
        
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
