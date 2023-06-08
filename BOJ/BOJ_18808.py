n, m, k = map(int, input().split())
shapes = []

graph = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    shape = [list(map(int, input().split())) for _ in range(r)]
    shapes.append(shape)

# 블럭이 들어갈 수 있는지 확인하는 로직
# def find_blank(shape):
#     len_x, len_y = len(shape), len(shape[0])
#     zero_pos = []
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 zero_pos.append((i, j))
    
#     possible_pos = []
#     for x, y in zero_pos:
#         flag = True
#         for i in range(len_x):
#             if flag == False:
#                 break
#             for j in range(len_y):
#                 if 0 <= x + i < n and 0 <= y + j < m:
#                     if shape[i][j] == 1 and graph[x + i][y + j] == 0:
#                         continue
#                     elif shape[i][j] == 0 and graph[x + i][y + j] == 1:
#                         continue
#                     elif shape[i][j] == 0 and graph[x + i][y + j] == 0:
#                         continue
#                     else:
#                         flag = False
#                         break
#                 else:
#                     flag = False
#                     break
                    
#         if flag == True:
#             # 하나만 체크
#             possible_pos.append((x, y))
#             break
    
    
#     # 만약 넣을 수 있는 칸이 있다면
#     if possible_pos:
#         for x, y in possible_pos:
#             for i in range(len_x):
#                 for j in range(len_y):
#                     graph[x + i][y + j] = shape[i][j]
#         return True
#     # 없으면 False 리턴
#     else:
#         return False
# 블럭이 들어갈 수 있는지 확인하는 로직
def find_blank(shape):
    len_x, len_y = len(shape), len(shape[0])

    for x in range(n - len_x + 1):
        for y in range(m - len_y + 1):
            flag = True
            for i in range(len_x):
                for j in range(len_y):
                    if 0 <= x + i < n and 0 <= y + j < m:
                        if shape[i][j] == 1 and graph[x + i][y + j] == 1:
                            flag = False
                            break
                        elif shape[i][j] == 1 and graph[x + i][y + j] == 0:
                            continue
                        elif shape[i][j] == 0:
                            continue
                    else:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                for i in range(len_x):
                    for j in range(len_y):
                        if shape[i][j] == 1:
                            graph[x + i][y + j] = 1
                return True
    return False


# 블록을 뒤집는 로직
def rotate(block):
    # 시계방향으로 90도 뒤집기
    block = list(map(list, zip(*block[::-1])))
    return block

for shape in shapes:
    if find_blank(shape):
        continue
    else:
        for i in range(3):
            shape = rotate(shape)
            if find_blank(shape):
                break

answer = 0
for i in graph:
    answer += i.count(1)
    # shape = rotate(shape)
    # print(shape)

print(answer)