# from collections import deque

# def solution(n, computers):
#     answer = 0
#     visited = [False for _ in range(n)]
#     for i in range(n):
#         if not visited[i]:
#             bfs(n, computers, i, visited)
#             answer += 1
#     return answer

# def bfs(n, computers, start, visited):
#     visited[start] = True
#     queue = deque()
#     queue.append(start)
#     while queue:
#         now = queue.popleft()
#         visited[now] = True
#         for i in range(n):
#             if i != now and computers[now][i] == 1:
#                 if not visited[i]:
#                     queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))