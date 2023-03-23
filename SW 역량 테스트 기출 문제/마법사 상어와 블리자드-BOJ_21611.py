n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
magic = []
result = [0] * 3
for _ in range(m):
    d, s = map(int, input().split())
    magic.append((d, s))

def destory(d, s):
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    
    x, y = (n - 1) // 2, (n - 1) // 2
    for i in range(1, s + 1):
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        # 파괴
        graph[nx][ny] = 0

def change_1D():
    init_graph = []
    x, y = (n - 1) // 2, (n - 1) // 2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    direct, move_count = 0, 0
    dist = 1
    
    while True:
        move_count += 1
        for i in range(dist):
            nx = x + dx[direct]
            ny = y + dy[direct]

            if (nx, ny) == (0, -1):
                return init_graph
            
            init_graph.append(graph[nx][ny])
            x, y = nx, ny
        
        if move_count == 2:
            dist += 1
            move_count = 0
        direct = (direct + 1) % 4

def move(init_graph):
    return [init_graph[i] for i in range(len(init_graph)) if init_graph[i] != 0]

def explore(init_graph):
    now_ball = init_graph[0]
    count = 1
    check_remove = False
    
    if not init_graph:
        return [], check_remove

    for i in range(1, len(init_graph)):
        if init_graph[i] == now_ball:
            count += 1
        else:
            if count >= 4:
                for j in range(1, count + 1):
                    init_graph[i - j] = 0
                result[now_ball - 1] += count
                check_remove = True
                count = 1
                now_ball = init_graph[i]
            else:
                count = 1
                now_ball = init_graph[i]
    
    if count >= 4:
        for i in range(1, count + 1):
            init_graph[len(init_graph) - i] = 0
        check_remove = True
        result[now_ball - 1] += count
    
    return init_graph, check_remove
                
def grouping(init_graph):
    if not init_graph:
        return []
    
    new_init_graph = []
    now_ball = init_graph[0]
    count = 1

    for i in range(1, len(init_graph)):
        if init_graph[i] == now_ball:
            count += 1
        else:
            new_init_graph.append(count)
            new_init_graph.append(now_ball)
            count = 1
            now_ball = init_graph[i]
    new_init_graph.append(count)
    new_init_graph.append(now_ball)
    return new_init_graph

def change_2D(init_graph):
    new_graph = [[0] * n for _ in range(n)]

    if not init_graph:
        return new_graph
    
    x, y = (n - 1) // 2, (n - 1) // 2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    direct, move_count = 0, 0
    count = 0
    dist = 1
    
    while True:
        move_count += 1
        for i in range(dist):
            nx = x + dx[direct]
            ny = y + dy[direct]

            if (nx, ny) == (0, -1):
                return new_graph
            
            new_graph[nx][ny] = init_graph[count]
            count += 1
            if len(init_graph) <= count:
                return new_graph
            x, y = nx, ny
        if move_count == 2:
            dist += 1
            move_count = 0
        direct = (direct + 1) % 4

for i in range(m):
    destory(magic[i][0], magic[i][1])
    init_graph = change_1D()
    init_graph = move(init_graph)
    while init_graph:
        init_graph, check_remove = explore(init_graph)
        if not check_remove:
            break
        init_graph = move(init_graph)
    graph = change_2D(grouping(init_graph))

print(result[0] + result[1] * 2 + result[2] * 3)