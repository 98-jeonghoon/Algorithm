def solution(n, paths, gates, summits):
    answer = []
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))
    def dijkstra():
        import heapq
        queue = []
        INF = int(1e9)
        distance = [INF] * (n + 1)
        
        for gate in gates:
            heapq.heappush(queue, (0, gate))
            distance[gate] = 0
        
        while queue:
            dist, now = heapq.heappop(queue)
            
            if now in summits_set or dist > distance[now]:
                continue
            for i in graph[now]:
                new_dist = max(dist,  i[1])
                if new_dist < distance[i[0]]:
                    distance[i[0]] = new_dist
                    heapq.heappush(queue, (new_dist, i[0]))
        min_intensity = [0, INF]
        for summit in summits:
            if distance[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = distance[summit]
        return min_intensity
                    
    
    summits.sort()
    summits_set = set(summits)
    return dijkstra()