n, m, x = map(int, input().split())

INF = int(1e9)
graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    import heapq
    distance = [INF] * (n + 1)
    queue = []
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

answer = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    answer = max(answer, go[x] + back[i])

print(answer)