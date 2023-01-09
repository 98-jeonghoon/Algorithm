# 삼성 SW 코테 문제에 벽을 느끼고 푸는 문제들

## 백준 1260 DFS와 BFS

# n, m, v = map(int, input().split())
# graph = [[] * m for _ in range(n+1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(n+1):
#     graph[i].sort()


# visited = [False] * (n+1)

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# dfs(graph, v, visited)


# visited = [False] * (n+1)
# from collections import deque

# def bfs(graph, v, visited):
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         now = queue.popleft()
#         print(now, end=' ')
#         for i in graph[now]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# print()         
# bfs(graph, v, visited)

## 바이러스 백준 2606번
# n = int(input())
# m = int(input())
# graph = [[] * m for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# for i in range(n):
#     graph[i].sort()
# visited = [False] * (n+1)

# count = 0
# def dfs(graph, v, visited):
#     global count
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             count += 1
#             dfs(graph, i, visited)

# dfs(graph, 1, visited)
# print(count)

## 단지번호붙이기 백준 2667번

# n = int(input())
# graph = [list(map(int, input())) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# count = 0
# def dfs(x,y):
#     global count
#     if x < 0 or y < 0 or x >= n or y >= n:
#         return
#     if graph[x][y] == 0:
#         return
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         count += 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)
#     return count

# arr = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             arr.append(dfs(i,j))
#             count = 0

# arr.sort()
# print(len(arr))
# for i in arr:
#     print(i)

## 유기농 배추 백준 1012
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def dfs(x, y):
#     global count
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return
#     if graph[x][y] == 0:
#         return
#     if graph[x][y] == 1:
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)

# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#     for i in range(k):
#         a, b = map(int, input().split())
#         graph[b][a] = 1
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 dfs(i, j)
#     print(count)

## 적록색약 백준 10026
# import sys
# sys.setrecursionlimit(10000)

# n = int(input())
# graph = [list(input()) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# visited = [[False] * n for _ in range(n)]
# def dfs(x, y):
#     visited[x][y] = True
#     current_color = graph[x][y]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<= nx < n and 0 <= ny < n:
#             if visited[nx][ny] == False and graph[nx][ny] == current_color:
#                 dfs(nx, ny)
                
# count = 0   
# for i in range(n):
#     for j in range(n):
#         if visited[i][j] == False:
#             dfs(i, j)
#             count += 1

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 'R':
#             graph[i][j] = 'G'

# visited = [[False] * n for _ in range(n)]

# RG_count = 0
# for i in range(n):
#     for j in range(n):
#         if visited[i][j] == False:
#             dfs(i, j)
#             RG_count += 1
            
# print(count, RG_count)

## 안전영역 백준 2468번
# import sys
# sys.setrecursionlimit(100000)
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# max_num = -1e9
# for i in range(n):
#     for j in range(n):
#         max_num = max(max_num, graph[i][j])

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def dfs(x, y, rain):
#     visited[x][y] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<= nx < n and 0<= ny < n:
#             if graph[nx][ny] > rain and visited[nx][ny] == False:
#                 dfs(nx, ny, rain)
          

# answer = 1
                
# for i in range(max_num):
#     visited = [[False] * n for _ in range(n)]
#     count = 0
#     for j in range(n):
#         for k in range(n):
#             if graph[j][k] > i and visited[j][k] == False:
#                 dfs(j, k, i)
#                 count += 1
#     answer = max(count, answer)
        
# print(answer)

# 알파벳 백준 1987

# r, c = map(int, input().split())
# graph = [list(map(lambda a : ord(a)-65,input())) for _ in range(r)]

# visited = [0] * 26
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# max_num = 1
# def dfs(x, y, count):
#     global max_num
#     if max_num < count:
#         max_num = count
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c:
#             if visited[graph[nx][ny]] == 0:
#                 visited[graph[nx][ny]] = 1
#                 dfs(nx, ny, count+1)
#                 visited[graph[nx][ny]] = 0
                
# visited[graph[0][0]] = 1
# dfs(0,0, max_num)
# print(max_num)

# def backtracing(start):
#     if len(arr) == 6:
#         print(*arr)
#         return
#     for i in range(start, len(num)):
#         if visited[i]:
#             continue
#         arr.append(num[i])
#         visited[i] = True
#         backtracing(i+1)
#         arr.pop()
#         visited[i] = False
# while True:
#     num = list(map(int,input().split()))
#     if num[0] == 0:
#         break
#     k = num.pop(0)
#     visited = [False] * len(num)
#     arr = []
#     backtracing(0)
#     print()

## 감시 백준 15683
# import copy
# n, m = map(int, input().split())
# cctv = []
# graph = []
# mode = [
#     [],
#     [[0], [1], [2], [3]],
#     [[0, 2], [1, 3]],
#     [[0, 1], [1, 2], [2, 3], [0, 3]],
#     [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
#     [[0, 1, 2, 3]],
# ]

# # 북 - 동 - 남 - 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# for i in range(n):
#     data = list(map(int, input().split()))
#     graph.append(data)
#     for j in range(m):
#         if data[j] in [1, 2, 3, 4, 5]:
#             cctv.append([data[j], i, j])

# def fill(board, mm, x, y):
#     for i in mm:
#         nx = x
#         ny = y
#         while True:
#             nx += dx[i]
#             ny += dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 break
#             if board[nx][ny] == 6:
#                 break
#             elif board[nx][ny] == 0:
#                 board[nx][ny] = 7

# def dfs(depth, arr):
#     global min_value

#     if depth == len(cctv):
#         count = 0
#         for i in range(n):
#             count += arr[i].count(0)
#         min_value = min(min_value, count)
#         return
#     temp = copy.deepcopy(arr)
#     cctv_num, x, y = cctv[depth]
#     for i in mode[cctv_num]:
#         fill(temp, i, x, y)
#         dfs(depth+1, temp)
#         temp = copy.deepcopy(arr)


# min_value = int(1e9)
# dfs(0, graph)
# print(min_value)

# from itertools import product
# def solution(n, x, y):
#     arr = []
#     arr.append(int(x))
#     arr.append(int(y))
#     data = []
#     for i in range(1, len(n)+1):
#         for j in product(arr, repeat=i):
#             data.append(''.join(map(str, j)))
#     answer = []
#     for i in data:
#         if int(i) < int(n):
#             answer.append(int(i))
#     return answer

# t = int(input())
# for i in range(t):
#     n, x, y = map(str, input().split())
#     answer = solution(n, x, y)
#     if len(answer) == 0 or max(answer) == 0:
#         print('#{} -1'.format(i+1))
#     else:
#         print('#{} {}'.format(i+1, max(answer)))


# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# max_value = -1e9
# def dfs(x, y, cnt, value):
#     global max_value
#     if cnt == 4:
#         max_value = max(max_value, value)
#         return
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
#             visited[nx][ny] = True
#             dfs(nx, ny, cnt + 1, value + graph[nx][ny])
#             visited[nx][ny] = False

# def pink(x, y):
#     global max_value
#     for i in range(4):
#         tmp = graph[x][y]
#         for j in range(3):
#             direction = (i + j) % 4
#             nx = x + dx[direction]
#             ny = y + dy[direction]
#             if not (0 <= nx < n and 0 <= ny < m):
#                 tmp = 0
#                 break
#             tmp += graph[nx][ny]
#         max_value = max(tmp, max_value)

# for i in range(n):
#     for j in range(m):
#         if visited[i][j]:
#             continue
#         visited[i][j] = True
#         dfs(i, j, 1, graph[i][j])
#         visited[i][j] = False
#         pink(i, j)
        
# print(max_value)
import copy
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_range = [
    [],
    [[0],[1],[2],[3]], #1번 카메라
    [[0,2],[1,3]], #2번 카메라
    [[0,1],[1,2],[2,3],[3,0]], #3번 카메라
    [[0,1,3],[0,1,2],[1,2,3],[0,2,3]], # 4번 카메라
    [[0,1,2,3]], # 5번 카메라
]

cctv = []
for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append([graph[i][j], i, j])

min_value = 1e9

def watch(graph, cctv_num, x, y):
    for i in cctv_num:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = '#'
            
def dfs(depth, arr):
    global min_value
    if len(cctv) == depth:
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(count, min_value)
        return
    
    tmp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in cctv_range[cctv_num]:
        watch(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(arr)
        
dfs(0, graph)
print(min_value)
            
                
    