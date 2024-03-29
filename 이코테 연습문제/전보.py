# 도시개수 n, 통로의 개수 m, 보내고자 하는 도시 c


import heapq
INF = int(1e9)
n, m, start = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    # a 에서 b로 가는데 c만큼 소요된다.
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
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

dijkstra(start)
print(distance)
count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)