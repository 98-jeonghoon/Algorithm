def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = []
    visited = [[False] * (len(maps[0])) for _ in range(len(maps))]
    def bfs(x, y):
        from collections import deque
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        count = int(maps[x][y])
        while queue:
            x, y =queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if visited[nx][ny] == False and maps[nx][ny] != 'X':
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        count += int(maps[nx][ny])
        return count
                        
            
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] != 'X' and visited[x][y] == False:
                count = bfs(x, y)
                answer.append(count)
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))