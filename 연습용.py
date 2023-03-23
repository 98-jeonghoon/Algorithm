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

# arr = list(map(int, input().split()))
# n, target = map(int, input().split())

# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == arr[mid]:
#             return mid
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# result = binary_search(arr, target, 0, n - 1)
# if result == None:
#     print('None')
# else:
#     print(result)

# n, m = map(int, input().split())
# trees = list(map(int, input().split()))

# start = 1
# end = max(trees)


# while start <= end:
#     mid = (start + end) // 2
    
#     total = 0
    
#     for tree in trees:
#         if tree > mid:
#             total += tree - mid
#     if total >= m:
#         start = mid + 1
#     else:
#         end = mid - 1

# print(end)

# k, n = map(int, input().split())
# lans = []
# for _ in range(k):
#     lan = int(input())
#     lans.append(lan)

# start = 1
# end = max(lans)

# def binary_search(lans, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         total = 0
        
#         for lan in lans:
#             total += lan // mid
        
#         if total >= n:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return end

# print(binary_search(lans, start, end))

# n = int(input())
# cards = list(map(int, input().split()))
# m = int(input())
# find = list(map(int, input().split()))

# cards.sort()

# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
        
#         if target == arr[mid]:
#             return True
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
            
#     return False

# for i in find:
#     result = binary_search(cards, i, 0, n - 1)
#     if result:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# n, c = map(int, input().split())
# arr = []
# for _ in range(n):
#     a = int(input())
#     arr.append(a)
# arr.sort()

# start = 1
# end = arr[-1] - arr[0]
# answer = 0
# def binary_search(arr, start, end):
#     global answer
#     while start <= end:
#         mid = (start + end) // 2
#         current = arr[0]
#         count = 1
#         for i in range(1, len(arr)):
#             if arr[i] >= current + mid:
#                 count += 1
#                 current = arr[i]
        
#         if count >= c:
#             start = mid + 1
#             answer = mid
#         else:
#             end = mid - 1
            
# binary_search(arr, start, end)
# print(answer)


n, m, k = map(int, input().split())
graph = [[[] * n for _ in range(n)] for _ in range(n)]
fire_ball = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fire_ball.append((r - 1, c - 1, m, s, d))



def print_graph():
    global graph
    for i in graph:
        print(i)

# print_graph()

for _ in range(k):
    while fire_ball:
        r, c, m, s, d = fire_ball.pop()
        nr = (r + s * dx[d]) % n
        nc = (c + s * dy[d]) % n
        graph[nr][nc].append((m, s, d))

    for x in range(n):
        for y in range(n):
            if len(graph[x][y]) >= 2:
                sum_m, sum_s, count, eval, odd = 0, 0, len(graph[x][y]), 0, 0
                while graph[x][y]:
                    m, s, d = graph[x][y].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        eval += 1
                    else:
                        odd += 1
                if count == eval or count == odd:
                    direct = [0, 2, 4, 6]
                else:
                    direct = [1, 3, 5, 7]
                if sum_m // 5:
                    for d in direct:
                        fire_ball.append((r, c, sum_m // 5, sum_s // count, d))
            if len(graph[x][y]) == 1:
                mm, ss, dd = graph[x][y].pop()
                fire_ball.append((x, y, mm, ss, dd))

answer = 0

for i in fire_ball:
    answer += i[2]
print(answer)