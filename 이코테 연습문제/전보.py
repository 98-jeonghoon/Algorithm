import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# x에서 y로 이동하는데 걸리는 비용 z
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
        
print(count - 1, max_distance)
    