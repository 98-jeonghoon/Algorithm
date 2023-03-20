n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
result = [0] * 3
magic = []

for _ in range(m):
    d, s = map(int, input().split())
    magic.append((d, s))

def destroy(d, s):
    global graph, n
    x, y = (n - 1) // 2, (n - 1) // 2
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    
    for i in range(1, s + 1):
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        graph[nx][ny] = 0
    
def change_1D():
    init_graph = []
    x, y = (n - 1) // 2, (n - 1) // 2
    tornado_dx = [0, 1, 0, -1]
    tornado_dy = [-1, 0, 1, 0]
    direct, move_count = 0, 0
    move = 1
    while True:
        move_count += 1
        for _ in range(move):
            nx = x + tornado_dx[direct]
            ny = y + tornado_dy[direct]
            if (nx, ny) == (0, -1):
                return init_graph
            init_graph.append(graph[nx][ny])
            x, y = nx, ny
        if move_count == 2:
            move += 1
            move_count = 0
        direct = (direct + 1) % 4

def remove_blank(init_graph):
    return [init_graph[i] for i in range(len(init_graph)) if init_graph[i] != 0]


def explode(arr):
    global result
    
    if not arr:
        return [], False
    
    now_ball = arr[0]
    count = 1
    check_remove = False
    
    for i in range(1, len(arr)):
        if arr[i] == now_ball:
            count += 1
        else:
            # 터지지 않을경우
            if count < 4:
                count = 1
                now_ball = arr[i]
            # 터질경우
            else:
                for j in range(1, count + 1):
                    arr[i - j] = 0
                result[now_ball - 1] += count
                check_remove = True
                count = 1
                now_ball = arr[i]
    if count >= 4:
        check_remove = True
        for j in range(1, count + 1):
            arr[len(arr) - j] = 0
        result[now_ball - 1] += count
    
    return arr, check_remove

def grouping(arr):
    if not arr:
        return []
    
    new_arr = []
    now_ball = arr[0]
    count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == now_ball:
            count += 1
        else:
            new_arr.append(count)
            new_arr.append(now_ball)
            count = 1
            now_ball = arr[i]
    new_arr.append(count)
    new_arr.append(now_ball)
    return new_arr

def change_2D(arr):
    new_graph = [[0] * n for _ in range(n)]
    if not arr:
        return new_graph
    
    tornado_dx = [0, 1, 0, -1]
    tornado_dy = [-1, 0, 1, 0]
    x, y = (n - 1) // 2, (n - 1) // 2
    direct, move_count = 0, 0
    move = 1
    arr_idx = 0
    while True:
        move_count += 1
        for _ in range(move):
            nx = x + tornado_dx[direct]
            ny = y + tornado_dy[direct]
            if (nx, ny) == (0, -1):
                return new_graph
            new_graph[nx][ny] = arr[arr_idx]
            arr_idx += 1
            if arr_idx >= len(arr):
                return new_graph
            x, y = nx, ny
        if move_count == 2:
            move += 1
            move_count = 0
        direct = (direct + 1) % 4

def solution():
    global result, m, graph, magic
    for i in range(m):
        destroy(magic[i][0], magic[i][1])
        arr = change_1D()
        arr = remove_blank(arr)
        while arr:
            arr, check_remove = explode(arr)
            if not check_remove:
                break
            arr = remove_blank(arr)
        graph = change_2D(grouping(arr))
    print(result[0] + 2 * result[1] + 3 * result[2])

solution()