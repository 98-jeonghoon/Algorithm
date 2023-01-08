import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctv_arr = []
cctv_range = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv_arr.append([graph[i][j], i, j])
            
def watch(board, move, x, y):
    for i in move:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = '#'

min_value = 1e9
def dfs(depth, arr):
    global min_value
    
    if depth == len(cctv_arr):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv_arr[depth]
    for i in cctv_range[cctv_num]:
        watch(temp, i, x, y)
        dfs(depth + 1, temp)
        temp = copy.deepcopy(arr)
        
dfs(0, graph)
print(min_value)