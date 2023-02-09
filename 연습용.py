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
# import copy
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# # 북 동 남 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# cctv_range = [
#     [],
#     [[0],[1],[2],[3]], #1번 카메라
#     [[0,2],[1,3]], #2번 카메라
#     [[0,1],[1,2],[2,3],[3,0]], #3번 카메라
#     [[0,1,3],[0,1,2],[1,2,3],[0,2,3]], # 4번 카메라
#     [[0,1,2,3]], # 5번 카메라
# ]

# cctv = []
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] in [1,2,3,4,5]:
#             cctv.append([graph[i][j], i, j])

# min_value = 1e9

# def watch(graph, cctv_num, x, y):
#     for i in cctv_num:
#         nx = x
#         ny = y
#         while True:
#             nx += dx[i]
#             ny += dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 break
#             if graph[nx][ny] == 6:
#                 break
#             elif graph[nx][ny] == 0:
#                 graph[nx][ny] = '#'
            
# def dfs(depth, arr):
#     global min_value
#     if len(cctv) == depth:
#         count = 0
#         for i in range(n):
#             count += arr[i].count(0)
#         min_value = min(count, min_value)
#         return
    
#     tmp = copy.deepcopy(arr)
#     cctv_num, x, y = cctv[depth]
#     for i in cctv_range[cctv_num]:
#         watch(tmp, i, x, y)
#         dfs(depth+1, tmp)
#         tmp = copy.deepcopy(arr)
        
# dfs(0, graph)
# print(min_value)

## 뱀 백준 3190

# n = int(input())
# graph = [[0] * n for _ in range(n)]
# k = int(input())
# for _ in range(k):
#     a, b = map(int, input().split())
#     graph[a-1][b-1] = 1

# dic = dict()
# l = int(input())
# for _ in range(l):
#     sec, dir = input().split()
#     dic[int(sec)] = dir

# from collections import deque

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def turn(direction, L_D_string):
#     if L_D_string == 'L':
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction

# def start():
#     direction = 1
#     nx, ny = 0, 0
#     queue = deque([[ny, nx]])
#     graph[ny][nx] = 2
#     time = 1
#     while True:
#         nx = nx + dx[direction]
#         ny = ny + dy[direction]
#         if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] != 2:
#             if not graph[ny][nx] == 1:
#                 tmp_y, tmp_x = queue.popleft()
#                 graph[tmp_y][tmp_x] = 0
#             graph[ny][nx] = 2
#             queue.append([ny, nx])
#             if time in dic.keys():
#                 direction = turn(direction, dic[time])
#             time += 1
#         else:
#             return print(time)

# start()


## 경사로 백준 14890

# n, l = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]


# answer = 0

# def pos(now):
#     for j in range(1, n):
#         if 1 < abs(now[j] - now[j-1]):
#             return False
#         if now[j] < now[j-1]:
#             for k in range(l):
#                 if j + k >= n or visited[j+k] or now[j] != now[j+k]:
#                     return False
#                 if now[j] == now[j+k]:
#                     visited[j+k] = True
#         elif now[j] > now[j-1]:
#             for k in range(l):
#                 if j - k - 1 < 0 or visited[j-k-1] or now[j-1] != now[j-k-1]:
#                     return False
#                 if now[j-1] == now[j-k-1]:
#                     visited[j -k -1] = True
#     return True

# answer = 4

# def dfs(depth, x, y):
#     global answer
#     if depth >= answer:
#         return
#     if check():
#         answer = min(answer, depth)
#     if depth == 3:
#         return
#     for i in range(x, h):
#         if i == x:
#             k = y
#         else:
#             k = 0
#         for j in range(k, n-1):
#             if graph[i][j] == 1:
#                 continue
#             graph[i][j] = 1
#             dfs(depth + 1, i, j + 2)
#             graph[i][j] = 0
            
# dfs(0, 0, 0)

# if answer <= 3:
#     print(answer)
# else:
#     print(-1)
    
# for i in range(n):
#     visited = [False] * (n+1)
#     if pos(graph[i]):
#         answer += 1
        
# for i in range(n):
#     visited = [False] * (n+1)
#     if pos([graph[j][i] for j in range(n)]):
#         answer += 1

# print(answer-1)

## 나무 재테크 백준 16235

# n, m, k = map(int, input().split())
# add_graph = [list(map(int, input().split())) for _ in range(n)]
# food_graph = [[5] * n for _ in range(n)]
# tree = [[[] for _ in range(n)] for _ in range(n)]
# for _ in range(m):
#     x, y, age = map(int, input().split())
#     tree[x-1][y-1].append(age)


# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# for _ in range(k):
#     for i in range(n):
#         for j in range(n):
#             if tree[i][j]:
#                 tree[i][j].sort()
#                 tmp_tree = []
#                 death_tree = 0
#                 for age in tree[i][j]:
#                     if food_graph[i][j] >= age:
#                         food_graph[i][j] -= age
#                         age += 1
#                         tmp_tree.append(age)
#                     else:
#                         death_tree += (age // 2)
#                 food_graph[i][j] += death_tree
#                 tree[i][j].clear()
#                 tree[i][j].extend(tmp_tree)

#     for i in range(n):
#         for j in range(n):
#             if tree[i][j]:
#                 for age in tree[i][j]:
#                     if age % 5 == 0:
#                         for dir in range(8):
#                             nx = i + dx[dir]
#                             ny = j + dy[dir]
#                             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                                 continue
#                             tree[nx][ny].append(1)

#     for i in range(n):
#         for j in range(n):
#             food_graph[i][j] += add_graph[i][j]

# answer = 0
# for i in range(n):
#     for j in range(n):
#         answer += len(tree[i][j])

# print(answer)


## 바이러스 백준 2606

# n = int(input())
# m = int(input())
# graph = [[] * m for _ in range(n + 1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited = [False] * (n + 1)

# for i in range(n + 1):
#     graph[i].sort()

# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
    
## 프로그래머스 lv3 정수 삼각형

# def solution(triangle):
#     dp = [[0] * len(triangle) for _ in range(len(triangle))]
#     dp[0][0] = triangle[0][0]

#     for i in range(0, len(triangle) - 1):
#         for j in range(len(triangle[i])):
#             dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
#             dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
#     return max(dp[-1])


# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


## 프로그래머스 lv3 네트워크

# def solution(n, computers):
#     answer = 0
#     visited = [False for _ in range(n)]
#     for i in range(n):
#         if visited[i] == False:
#             dfs(n, computers, visited, i)
#             answer += 1
#     return answer
# def dfs(n, computers, visited, start):
#     visited[start] = True
#     for i in range(n):
#         if i != start and computers[start][i] == 1:
#             if not visited[i]:
#                 dfs(n, computers, visited, i)

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# def solution(k, dungeons):
#     from itertools import permutations
#     answer = 0
#     dungeons = list(permutations(dungeons, len(dungeons)))
#     for dun in dungeons:
#         count = 0
#         firo = k
#         for need, use in dun:
#             if need > firo:
#                 break
#             else:
#                 firo -= use
#                 count += 1
#         answer = max(answer, count)
#     return answer
    
    
# print(solution(80, [[80,20],[50,40],[30,10]]))

# def solution(word):
#     answer = 0
#     arr = []
#     from itertools import product
#     alpha = ['A', 'E', 'I', 'O', 'U']
#     for i in range(1, len(alpha) + 1):
#         case = list(product(alpha, repeat=i))
#         for j in case:
#             arr.append(''.join(j))
#     arr.sort()
#     return arr.index(word) + 1

# print(solution('AAAAE'))

# def solution(m, n, board):
#     answer = 0
#     map = []
#     for i in range(m):
#         map.append(list(board[i]))
#     remove = set()
    
#     while True:
#         for i in range(m - 1):
#             for j in range(n - 1):
#                 now = map[i][j]
#                 if map[i][j] == 0:
#                     continue
#                 if map[i+1][j] == now and map[i][j+1] == now and map[i+1][j+1] == now:
#                     remove.add((i, j))
#                     remove.add((i+1, j))
#                     remove.add((i, j+1))
#                     remove.add((i+1,j+1))
                    
#         if remove:
#             answer += len(remove)
#             for a, b in remove:
#                 map[a][b] = 0
#             remove = set()
#         else:
#             return answer
        
#         while True:
#             cnt = 0
#             for i in range(m - 1):
#                 for j in range(n):
#                     if map[i][j]:
#                         if map[i + 1][j] == 0:
#                             map[i + 1][j] = map[i][j]
#                             map[i][j] = 0
#                             cnt = 1
#             if cnt == 0:
#                 break
        

# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

# def solution(s):
#     arr = []
#     n = len(s) // 2
#     if len(s) == 1:
#         return 1
    
#     for i in range(1, n+1):
#         tmp = ''
#         count = 1
#         compare = s[:i]
#         for j in range(i, len(s), i):
#             if compare == s[j:j+i]:
#                 count += 1
#             else:
#                 if count != 1:
#                     tmp += str(count) + compare
#                 else:
#                     tmp += compare
#                 compare = s[j:j+i]
#                 count = 1
#         if count != 1:
#             tmp += str(count) + compare
#         else:
#             tmp += compare
#         arr.append(len(tmp))
#     return min(arr)

# print(solution("aabbaccc"))

# def solution(queue1, queue2):
#     answer = 0
#     count = 0
#     num = (sum(queue1) + sum(queue2)) // 2
#     from collections import deque
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     limit = len(queue1) * 3
#     while True:
#         if sum(queue1) ==num and sum(queue2) == num:
#             break
#         elif sum(queue1) > sum(queue2):
#             queue2.append(queue1.popleft())
#             count += 1
#         elif sum(queue1) < sum(queue2):
#             queue1.append(queue2.popleft())
#             count += 1
        
#         if count == limit:
#             count = -1
#             break
                      
#     return count

# print(solution([3,2,7,2], [4,6,5,1]))

# def solution(orders, course):
#     from itertools import combinations
#     from collections import Counter
#     answer = []
#     for i in course:
#         arr = []
#         for j in orders:
#             arr += list(combinations(j, i))
#         counter = Counter(arr)
#         # print(counter)
#         if len(counter) == 0:
#             continue
#         if max(counter.values()) == 1:
#             continue
#         for f in counter:
#             if counter[f] == max(counter.values()):
#                 answer.append(''.join(f))
#     # answer = list(set(answer))
#     print(answer)
            
    # for order in orders:
    #     for i in range(1, len(order) + 1):
    #         for j in combinations(order, i):
    #             arr.append(''.join(j))
    # arr = Counter(arr)
    # arr = list(arr.items())
    # arr.sort(key=lambda x : x[1], reverse=True)
    # print(arr)
#     return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))


# from collections import deque

# def solution(s):
#     answer = 0
#     s = deque(s)
#     for _ in range(len(s)):
#         if is_Valid(s):
#             answer += 1
#         s.rotate(-1)
#     return answer

# def is_Valid(s):
#     arr = []
#     for i in s:
#         if arr == []:
#             arr.append(i)
#         else:
#             if i == ')' and arr[-1] == '(':
#                 arr.pop()
#             elif i == ']' and arr[-1] == '[':
#                 arr.pop()
#             elif i == '}' and arr[-1] == '{':
#                 arr.pop()
#             else:
#                 arr.append(i)
#     if arr == []:
#         return True
#     else:
#         return False

# print(solution('[](){}'))


# def solution(progresses, speeds):
#     answer = []
#     arr = []
#     for i in range(len(progresses)):
#         count = 0
#         while True:
#             count += 1
#             progresses[i] += speeds[i]
#             if progresses[i] >= 100:
#                 break
#         arr.append(count)
#     from collections import deque
#     queue = deque(arr)
#     while queue:
#         tmp = queue.popleft()
#         cnt = 1
#         while queue and tmp >= queue[0]:
#             queue.popleft()
#             cnt += 1
#         answer.append(cnt)
        
#     return answer


# print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))
# def solution(priorities, location):
#     from collections import deque
#     answer = 0
#     arr = []
#     for idx, prior in enumerate(priorities):
#         arr.append((idx, prior))
#     queue = deque(arr)

#     while queue:
#         max_prior = max(queue, key=lambda x:x[1])[1]
#         idx, prior = queue.popleft()
#         if queue and prior < max_prior:
#             queue.append((idx, prior))
#         else:
#             answer += 1
#             if idx == location:
#                 break
        
#     return answer

# print(solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1))
# print(solution([2, 1, 3, 2], 2))
# print(solution([1,1,9,1,1,1], 0))

# from collections import deque
# def solution(numbers, target):
#     answer = 0
#     n = len(numbers)
#     def back_tracking(depth, result):
#         if depth == n:
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#         else:
#             back_tracking(depth + 1, result + numbers[depth])
#             back_tracking(depth + 1, result - numbers[depth])
#     back_tracking(0, 0)
#     return answer
# print(solution([1,1,1,1,1], 3))

# def solution(scoville, K):
#     import heapq
#     answer = 0
#     while True:
#         heapq.heapify(scoville)
#         if len(scoville) == 1 and scoville[0] < K:
#             return -1

#         first = heapq.heappop(scoville)
#         if first < K:
#             answer += 1
#             second = heapq.heappop(scoville) * 2
#             heapq.heappush(scoville, first + second)
#         else:
#             return answer
        

# print(solution([1, 2, 3, 9, 10, 12], 7))

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        s = ''
        for i in tree:
            if i in skill:
                s += i
        if skill[:len(s)] == s:
            answer += 1
    return answer

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]	))