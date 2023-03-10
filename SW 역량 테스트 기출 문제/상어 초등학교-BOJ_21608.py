n = int(input())
students = []
graph = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n**2):
    students.append((list(map(int, input().split()))))
    
for order in range(n**2):
    student = students[order]
    tmp = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0:
                like = 0
                blank = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in student[1:]:
                            like += 1
                        if graph[nx][ny] == 0:
                            blank += 1
                tmp.append((like, blank, x, y))
    tmp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    graph[tmp[0][2]][tmp[0][3]] = student[0]


students.sort()

answer = 0
for x in range(n):
    for y in range(n):
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in students[graph[x][y] - 1]:
                    count += 1
        if count != 0:
            answer += 10 ** (count - 1)
            
print(answer)