n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(dir, graph):
    # 위쪽
    if dir == 0:
        for y in range(n):
            pointer = 0
            for x in range(1, n):
                if graph[x][y]:
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    if graph[pointer][y] == 0:
                        graph[pointer][y] = tmp
                    elif graph[pointer][y] == tmp:
                        graph[pointer][y] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        graph[pointer][y] = tmp
    
    # 아래쪽
    elif dir == 1:
        for y in range(n):
            pointer = n - 1
            for x in range(n-2, -1, -1):
                if graph[x][y]:
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    if graph[pointer][y] == 0:
                        graph[pointer][y] = tmp
                    elif graph[pointer][y] == tmp:
                        graph[pointer][y] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        graph[pointer][y] = tmp
    
    # 왼쪽
    elif dir == 2:
        for x in range(n):
            pointer = 0
            for y in range(1, n):
                if graph[x][y]:
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    if graph[x][pointer] == 0:
                        graph[x][pointer] = tmp
                    elif graph[x][pointer] == tmp:
                        graph[x][pointer] = tmp * 2
                        pointer += 1
                    else:
                        pointer += 1
                        graph[x][pointer] = tmp

    # 오른쪽
    else:
        for x in range(n):
            pointer = n - 1
            for y in range(n - 2, -1, -1):
                if graph[x][y]:
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    if graph[x][pointer] == 0:
                        graph[x][pointer] = tmp
                    elif graph[x][pointer] == tmp:
                        graph[x][pointer] = tmp * 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        graph[x][pointer] = tmp

    return graph

import copy
answer = 0
def back_tracking(depth, graph):
    global answer
    if depth == 5:
        for x in range(n):
            for y in range(n):
                answer = max(answer, graph[x][y])
        return

    for i in range(4):
        tmp_graph = move(i, copy.deepcopy(graph))
        back_tracking(depth + 1, tmp_graph)

back_tracking(0, graph)
print(answer)