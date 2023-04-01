def bfs(arr):
    from collections import deque
    start = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(5):
        for y in range(5):
            if arr[x][y] == 'P':
                start.append([x, y])
    
    for x, y in start:
        queue = deque()
        queue.append((x, y))
        visited = [[False] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[x][y] = 1
        
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                    if arr[nx][ny] == 'O':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                    if arr[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place)) 
    return answer
        
        
        
            
        
    
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))