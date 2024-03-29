#간단한 다익스트라 알고리즘 구현
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n,m = map(int,input().split())
# start = int(input())

# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance =[INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
    
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]: 
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] =j[1]
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost =distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
                
# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

# # 힙을 이용한 구현
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# # n = 노드의 개수, m = 간선의 개수

# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)

# for _ in range(m):
#     # a번 노드에서 b번 노드로 가는 비용이 c이다
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
    
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
            
            
# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])
 
# import heapq

# # 노드수, 간선수
# n, m = map(int, input().split())
# # 시작 노드
# start = int(input())
# INF = int(1e9)

# distance = [INF] * (n + 1)
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     # a 노드에서 b 노드까지 가는 비용이 c이다.
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# def dijkstra(start):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     distance[start] = 0

#     while queue:
#         dist, now = heapq.heappop(queue)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(queue, (cost, i[0]))

# dijkstra(start)
# print(distance)
# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print(INF)
#     else:
#         print(distance[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (n + 1)

def dijkstra(start):
    import heapq
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

for i in range(1, n + 1):
    if distance[i] == INF:
        print(INF)
    else:
        print(distance[i])
    