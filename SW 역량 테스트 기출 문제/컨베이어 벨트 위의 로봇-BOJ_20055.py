from collections import deque

n, k = map(int, input().split())
belt = list(map(int ,input().split()))
belt = deque(belt)

visited = [0] * n
visited = deque(visited)
answer = 0
while True:
    belt.rotate(1)
    visited.rotate(1)
    visited[-1] = 0
    if sum(visited):
        for i in range(n-2, -1, -1):
            if visited[i] == 1 and visited[i+1] == 0 and belt[i+1] >= 1:
                visited[i+1] = 1
                belt[i+1] -= 1
                visited[i] = 0
            visited[-1] = 0
    if visited[0] == 0 and belt[0] >= 1:
        visited[0] = 1
        belt[0] -= 1
    answer += 1
    if belt.count(0) >= k:
        break
    
print(answer)