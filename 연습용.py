# # 시간초과 코드 O(n^2)
# n = int(input())
# work = list(map(int, input().split()))
# not_work = list(map(int, input().split()))
# answer = 0
# for i in range(n):
#     calc = sum(work[i:]) + sum(not_work[:i])
#     calc2 = sum(not_work[i:]) + sum(work[:i])
#     add = max(calc2, calc)
#     answer = max(answer, add)

# print(answer)


# # solve 코드 O(n)
# n = int(input())
# work = list(map(int, input().split()))
# not_work = list(map(int, input().split()))


# cum_work = [0] * (n+1)
# cum_not_work = [0] * (n+1)
# for i in range(n):
#     cum_work[i+1] = cum_work[i] + work[i]
#     cum_not_work[i+1] = cum_not_work[i] + not_work[i]

# answer = 0
# for i in range(n+1):
#     calc = cum_work[i] + cum_not_work[n] - cum_not_work[i]
#     calc2 = cum_not_work[i] + cum_work[n] - cum_work[i]
#     add = max(calc2, calc)
#     answer = max(answer, add)

# print(answer)

# import copy
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# cctv_arr = [
#     [],
#     [[0], [1], [2], [3]],
#     [[0, 1], [2, 3]],
#     [[0, 3], [3, 1], [1, 2], [2, 0]],
#     [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
#     [[0, 1, 2, 3]]
# ]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# cctv = []
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] > 0 and graph[i][j] < 6:
#             cctv.append((i, j, graph[i][j]))


# def watch(board, move, x, y):
#     for i in move:
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
#                 board[nx][ny] = '#'
                

# min_value = 1e9

# def backtracking(depth, graph):
#     global min_value
    
#     if depth == len(cctv):
#         count = 0
#         for i in range(n):
#             count += graph[i].count(0)
#         min_value = min(min_value, count)
#         return
    
#     temp_graph = copy.deepcopy(graph)
#     x, y, cctv_num = cctv[depth]
#     for i in cctv_arr[cctv_num]:
#         watch(temp_graph, i, x, y)
#         backtracking(depth + 1, temp_graph)
#         temp_graph = copy.deepcopy(graph)
        
# backtracking(0, graph)
# print(min_value)

