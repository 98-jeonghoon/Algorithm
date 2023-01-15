n, m, k = map(int, input().split())
add_graph = [list(map(int, input().split())) for _ in range(n)]
food_graph = [[5] * n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                tmp_tree = []
                death_tree = 0
                for age in tree[i][j]:
                    if food_graph[i][j] >= age:
                        food_graph[i][j] -= age
                        age += 1
                        tmp_tree.append(age)
                    else:
                        death_tree += (age // 2)
                food_graph[i][j] += death_tree
                tree[i][j].clear()
                tree[i][j].extend(tmp_tree)

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            nx = i + dx[dir]
                            ny = j + dy[dir]
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            tree[nx][ny].append(1)

    for i in range(n):
        for j in range(n):
            food_graph[i][j] += add_graph[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer)

# for t in range(k):
#     sorted(queue, key= lambda x : (x[2], x[0], x[1]))
#     for _ in range(len(queue)):
#         x, y, age = queue.popleft()
#         if food_graph[x][y] >= age:
#             food_graph[x][y] -= age
#             age += 1
#             if age % 5 == 0:
#                 for i in range(8):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if nx < 0 or nx >=n or ny < 0 or ny >= n:
#                         continue
#                     queue.append((nx, ny, 1))
#             else:
#                 queue.append((x, y, age))
#         else:
#             food_graph[x][y] += (age // 2)
#     for i in range(n):
#         for j in range(n):
#             food_graph[i][j] += add_graph[i][j]

# print(len(queue))
