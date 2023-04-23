# 시계방향으로 회전하는 코드 list(map(list, zip(*arr[::-1])))
# 시계 반대방향으로 회전하는 코드 list(map(list, zip(*arr)))[::-1]


n, k = map(int, input().split())
fish_bowl = list(map(int, input().split()))
graph = [[fish] for fish in fish_bowl]

print(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate(x, y):
    temp_grounds = [[0] * x for _ in range(y)]

    for r in range(x):
        for c in range(y):
            temp_grounds[c][x - r - 1] = cur_graph[r][c]
    return temp_grounds

def cal_fish():
    global graph
    temp_graph = [[0] * len(graph[0]) for _ in range(len(graph))]
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] == - 1:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if graph[nx][ny] == - 1:
                        continue
                    calc = graph[x][y] - graph[nx][ny]
                    calc //= 5
                    if calc <= 0:
                        continue
                    temp_graph[nx][ny] += calc
                    temp_graph[x][y] -= calc
    
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            graph[x][y] += temp_graph[x][y]
    return

def make_one():
    global graph
    temp_graph = []
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] != -1:
                temp_graph.append(graph[x][y])
    graph = temp_graph
    return

result = 0
while True:
    min_value = 1e9
    max_value = -1e9
    for i in graph:
        min_value = min(i[0], min_value)
        max_value = max(i[0], max_value)
    if max_value - min_value <= k:
        break
    result += 1
    
    for i in range(len(graph)):
        if graph[i][0] == min_value:
            graph[i][0] += 1
            
    up_to_fish = graph.pop(0)
    graph[0].extend(up_to_fish)
    
    while True:
        idx = 0 
        while len(graph[idx]) >= 2:
            idx += 1
            if len(graph) - idx < len(graph[0]):
                break
        
        if len(graph) - idx < len(graph[0]):
            break
    
        cur_graph = []
        for _ in range(idx):
            cur_graph.append(graph.pop(0))
        
        ready_graph = rotate(idx, len(cur_graph[0]))
        for i in range(len(ready_graph)):
            graph[i].extend(ready_graph[i])
            
    height = len(graph[0])
    for i in range(len(graph)):
        while len(graph[i]) < height:
            graph[i].append(-1)
            
    cal_fish()
    
    make_one()
    
    for _ in range(2):
        idx = len(graph) // 2
        temp_graph = []
        while idx:
            temp_graph.append(graph.pop(0))
            idx -= 1
            
        if type(temp_graph[0]) == list:
            rever_temp = [[0] * len(temp_graph[0]) for _ in range(len(temp_graph))]
            for i in range(len(temp_graph)):
                for j in range(len(temp_graph[0])):
                    rever_temp[i][j] = temp_graph[i][len(temp_graph[0]) - j - 1]
            
            for i in range(len(graph)):
                graph[i].extend(rever_temp.pop())
        
        else:
            graph = [[i] for i in graph]
            
            for i in range(len(graph)):
                graph[i].append(temp_graph.pop())
                
    
    cal_fish()
    
    make_one()
    
    graph = [[i] for i in graph]
    
print(result)