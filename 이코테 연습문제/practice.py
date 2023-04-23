# n, m, k = map(int,input().split())
# graph = [[[] for _ in range(n)]  for _ in range(n)]
# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(n):
#         if data[j] == 0:
#             continue
#         else:
#             graph[i][j].append(data[j])
# # player_map = [[0]*n for i in range(n)]
# plys_pos = []
# plys_dp  = []
# plys_gun = [0]*m
# plys_point = [0]*m
# for i in range(m):
#     x, y, d, s = map(int,input().split())
#     plys_pos.append([x-1,y-1])
#     plys_dp.append([d,s])

# def print_gr(graph):
#     print("=============")
#     for i in range(n):
#         print(graph[i])

# dx = [-1,0,1,0]
# dy = [0, 1,0,-1]

# def turn90(direction):
#     return (direction+1)%4
# def turn180(directions):
#     return (directions+2)%4


# def change_gun(x,y,pi):
#     if graph[x][y] == []:
#         return
#     else:
#         if plys_gun[pi] == 0:
#             graph[x][y].sort()
#             plys_gun[pi] = graph[x][y][-1]
#             graph[x][y] = graph[x][y][:-1]
#         else:
#             graph[x][y].append(plys_gun[pi])
#             graph[x][y].sort()
#             plys_gun[pi] = graph[x][y][-1]
#             graph[x][y] = graph[x][y][:-1]

# def put_down(pi):
#     x,y = plys_pos[pi]
#     if plys_gun[pi] == 0:
#         return
#     else:
#         graph[x][y].append(plys_gun[pi])
#         plys_gun[pi] = 0

# def fight(i,j):
#     if plys_dp[i][1]+plys_gun[i] > plys_dp[j][1]+plys_gun[j]:
#         win,loo = i,j
#     elif plys_dp[i][1]+plys_gun[i] < plys_dp[j][1]+plys_gun[j]:
#         win, loo = j, i
#     else:
#         if plys_dp[i][1] > plys_dp[j][1]:
#             win, loo = i, j
#         else:
#             win, loo = j, i

#     plys_point[win] += abs((plys_dp[i][1]+plys_gun[i]) - (plys_dp[j][1]+plys_gun[j]))

#     put_down(loo)
#     x, y = plys_pos[loo]
#     d = plys_dp[loo][0]
#     for i in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if nx >= n or nx < 0 or ny >= n or ny < 0:
#             d = turn90(d)
#         elif [nx,ny] in plys_pos:
#             d = turn90(d)
#         else:
#             plys_pos[loo] = [nx,ny]
#             plys_dp[loo][0] = d
#             change_gun(nx,ny,loo)
#             break
#     x,y = plys_pos[win]
#     change_gun(x,y,win)


# def move():
#     for i in range(len(plys_pos)):
#         x,y = plys_pos[i]
#         d   = plys_dp[i][0]
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if nx>=n or nx < 0 or ny>=n or ny <0:
#             d = turn180(d)
#             nx = x + dx[d]
#             ny = y + dy[d]

#         if [nx,ny] in plys_pos:
#             counter = plys_pos.index([nx, ny])
#             plys_pos[i]   = [nx,ny]
#             plys_dp[i][0] = d
#             fight(i,counter)
#         else:
#             plys_pos[i]   = [nx,ny]
#             plys_dp[i][0] = d
#             change_gun(nx,ny,i)

# # print(plys_pos)
# for i in range(k):
#     move()
#     # print("[i]: ",i)
#     # print(plys_pos)
#     # print("dp : ",plys_dp)
#     # print("guns",plys_gun)
#     # print(plys_point)
#     # print_gr(graph)
#     # input()

# for i in range(m):
#     print(plys_point[i], end = " ")


