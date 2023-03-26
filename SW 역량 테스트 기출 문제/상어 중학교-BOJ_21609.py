# # 시계방향으로 회전하는 코드 list(map(list, zip(*arr[::-1])))
# # 시계 반대방향으로 회전하는 코드 list(map(list, zip(*arr)))[::-1]
# # 1트 실패 -> 조건 1번에 같은 블록 그룹이 여러개일때를 처리 해주지 못해서 막혔음.
# # 2트 성공 -> 무지개 블록과 일반 블록을 따로 구해줌

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, now):
    queue = deque()
    queue.append((x, y))
    block_cnt, rainbow_cnt = 1, 0
    block, rainbow = [[x, y]], []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 일반 블록
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] == now:
                visited[nx][ny] = True
                queue.append((nx, ny))
                block_cnt += 1
                block.append([nx, ny])
            
            # 무지개 블록
            elif 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                block_cnt += 1
                rainbow_cnt += 1
                rainbow.append([nx, ny])
    for x, y in rainbow:
        visited[x][y] = False
    
    return [block_cnt, rainbow_cnt, block + rainbow]

def remove(block):
    for x, y in block:
        graph[x][y] = -2
        
def gravity():
    for i in range(n-1, -1, -1):
        for j in range(n):
            if graph[i][j] > -1:
                tmp = i
                while True:
                    if 0<=tmp+1<n and graph[tmp+1][j] == -2:
                        graph[tmp+1][j] = graph[tmp][j]
                        graph[tmp][j] = -2
                        tmp += 1
                    else:
                        break

def rotate_90(graph):
    graph = list(map(list, zip(*graph)))[::-1]
    return graph

answer = 0

while True:
    blocks = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = bfs(i, j, graph[i][j])
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks = sorted(blocks, key= lambda x : (-x[0], -x[1], -x[2][0][0], -x[2][0][1]))
    # print(blocks)
    # print()

    if not blocks:
        break
    remove(blocks[0][2])
    answer += blocks[0][0] ** 2
    gravity()
    graph = rotate_90(graph)
    gravity()
    
print(answer)