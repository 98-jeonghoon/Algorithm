# def solution(n):
#     answer = []
#     graph = [[0] * i for i in range(1, n+1)]
#     x, y = -1, 0
#     num = 1
#     for i in range(n):
#         for j in range(i, n):
#             if i % 3 == 0:
#                 x += 1
#             elif i % 3 == 1:
#                 y += 1
#             else:
#                 x -= 1
#                 y -= 1
#             graph[x][y] = num
#             num += 1
#     # 아래쪽으로 쭉 내려가면서 값 더해주기    
#     return sum(graph, [])

# print(solution(4))

def solution(n):
    graph = [[0] * i for i in range(1, n+1)]
    # 하, 우, 왼쪽으로 올라가는 대각선
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x, y = 0, 0
    total = sum(list(i for i in range(1, n+1)))
    d = 0
    count = 1
    while count <= total:
        graph[x][y] = count
        count += 1
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            d = (d+1) % 3
            x += dx[d]
            y += dy[d]
    arr = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            arr.append(graph[i][j])
    print(arr)
    return sum(graph, [])
        
    
print(solution(4))























