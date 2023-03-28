n, m = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
INF = int(1e9)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    import heapq
    queue = []
    distance = [INF] * (n + 1)
    heapq.heappush(queue, (0, start))
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

v1, v2 = map(int, input().split())
first = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = first[v1] + v1_distance[v2] + v2_distance[n]
v2_path = first[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)

if result < INF:
    print(result)
else:
    print(-1)