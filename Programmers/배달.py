def solution(N, road, K):
    graph = [[] * (N + 1) for _ in range(N + 1)]
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))
    
    distance = dijkstra(1, N, graph)
    count = 0
    for i in distance:
        if i <= K:
            count += 1
    return count

def dijkstra(start, N, graph):
    import heapq
    INF = int(1e9)
    distance = [INF] * (N + 1)
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

                