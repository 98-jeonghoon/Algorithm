n, m, r = map(int, input().split())
item = list(map(int, input().split()))

graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
INF = int(1e9)

def dijkstra(start):
    import heapq
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

answer = 0
for i in range(1, n + 1):
    distance = dijkstra(i)
    count = 0
    for d in range(len(distance)):
        if distance[d] <= m:
            count += item[d - 1]
        answer = max(answer, count)
print(answer)