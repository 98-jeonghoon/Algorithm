n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def pos(now):
    for j in range(1, n):
        if abs(now[j] - now[j-1]) > 1:
            return False
        if now[j] < now[j-1]:
            for k in range(l):
                if j + k >= n or visited[j + k] or now[j] != now[j+k]:
                    return False
                if now[j] == now[j+k]:
                    visited[j + k] = True
        elif now[j] > now[j - 1]:
            for k in range(l):
                if j - k - 1 < 0 or now[j - 1] != now[j - k -1] or visited[j -k -1]:
                    return False
                if now[j - 1] == now[j -k - 1]:
                    visited[j -k -1] = True
    return  True

for i in range(n):
    visited = [False] * n
    if pos(graph[i]):
        answer += 1
    
for i in range(n):
    visited = [False] * n
    if pos([graph[j][i] for j in range(n)]):  # 현재 확인할 길을 넣어준다.
        answer += 1
        
print(answer)