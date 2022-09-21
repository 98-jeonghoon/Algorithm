# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))


# def dfs(x,y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)
#         return True
#     return False

                
# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     count = 0
#     graph = [[0]*m for _ in range(n)]

#     for _ in range(k):
#         a, b = map(int , input().split())
#         graph[b][a] = 1
    
#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j) == True:
#                 count += 1
#     print(count)

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid -1
#         else:
#             start = mid + 1
#     return None

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print('원소 존재 하지 않음')
# else:
#     print(result + 1)


# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print('원소 존재 X')
# else:
#     print(result+1)



# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:   
#             start = mid + 1
#     return None
            
# n, target = map(int , input().split())
# array = list(map(int , input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print('none')
# else:
#     print(result + 1)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
# n = 노드, m = 간선
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
# a노드에서 b노드로 이동하는 c비용
# b는 node, c는 비용
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    # 거리, 노드
    heapq.heappush(q, (0, start))
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

for i in range(1, n+1):
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])