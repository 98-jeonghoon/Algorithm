# 봄 -> 자신의 나이만큼 양분을 먹고 나이가 1증가
# 한칸에 여러개의 나무가 있다면 나이가 어린 나무부터 양분을 먹는다.
# 만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽음

# 여름 -> 죽은 나무가 양분으로 변하게 된다. 죽은 나무마다 나이를 2로 나눈값이
# 나무가 있던 칸에 양분으로 추가

# 가을 -> 나무 번식한다. 나무는 나이가 5의 배수여야하며, 8개의 인접칸에 나이가 1인 나무가 생김

# 겨울 -> 땅에 양분을 추가한다.

# k년후 살아있는 나무의 개수를 구하라



n, m, k = map(int, input().split())

# 초기 그래프 설정
# 나무가 칸마다 여러개가 있을수 있으므로 3차원 배열으로 선언
graph = [[[] for _ in range(n)] for _ in range(n)]
# 초기 양분그래프
food_graph = [[5] * n for _ in range(n)]
# 양분의 정보가 담긴 그래프 선언
add_graph = [list(map(int, input().split())) for _ in range(n)]

# 나무의 위치를 입력받아 그래프에 초기화하기
for _ in range(m):
    x, y, age = map(int, input().split())
    graph[x - 1][y - 1].append(age)

# 봄 여름 가을 겨울 반복
def spring():
    # 자신의 나이만큼 양분을 먹어야함
    # 나무가 존재하는 위치를 찾아줌
    tree_pos = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                # 어린 나무부터 시작하도록 정렬해준다.
                graph[i][j].sort()
                # 나무의 위치를 기록해준다.
                tree_pos.append((i, j))
    
    # 죽은 나무를 기록하기 위한 배열 선언
    death_pos = []
    for x, y in tree_pos:
        for i in range(len(graph[x][y])):
            # 만약 양분을 먹을 수 있다면
            if graph[x][y][i] <= food_graph[x][y]:
                # 나무가 자신의 나이 만큼 양분을 먹고
                food_graph[x][y] -= graph[x][y][i]
                # 나무의 나이를 1 증가시킨다
                graph[x][y][i] += 1

            # 만약 나무가 자신의 나이만큼 양분을 먹을 수 없다면
            else:
                # 바로 죽는다
                # 죽은 나무를 배열에 추가하고
                death_pos.append((x, y, graph[x][y][i]))
                # 0으로 값을 바꿔줌
                graph[x][y][i] = 0
    
    # 죽은 나무를 제거해줌
    for x, y in tree_pos:
        for _ in range(len(graph[x][y])):
            # 하나씩 나무를 꺼내와서
            now = graph[x][y].pop(0)
            # 만약 나무가 0, 즉 죽었다면 그냥 진행
            if now == 0:
                continue
            # 죽지 않았다면 다시 그래프에 추가해줌
            elif now > 0:
                graph[x][y].append(now)
            
    
    # 죽은 나무가 존재하면 죽은 나무의 위치를 리턴
    if death_pos:
        return death_pos
    # 죽은 나무가 없다면 None값을 리턴
    else:
        return None

def summer(death_pos):
    # 만약 죽은 나무가 없다면 바로 리턴
    if death_pos == None:
        return
    # 죽은 나무가 양분으로 변하게 된다.
    for x, y, age in death_pos:
        # 죽은 나무마다 나이를 2로 나눈 값이 추가됨
        age = age // 2
        # 나눈값을 양분 그래프에 추가
        food_graph[x][y] += age

def autumn():
    # 나무가 번식한다.
    # 번식은 총 8개의 칸으로 번식함
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    # 나무가 존재하는 칸을 확인하여 tree_pos에 넣어줌
    tree_pos = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                tree_pos.append((i, j))
    
    for x, y in tree_pos:
        for i in range(len(graph[x][y])):
            # 만약 번식하는 나무의 나이가 5의 배수이면
            if graph[x][y][i] % 5 == 0:
                # 8개 칸으로 번식을 진행함
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 범위를 벗어나지 않는다면
                    if 0 <= nx < n and 0 <= ny < n:
                        # 나이가 1인 나무가 생긴다.
                        graph[nx][ny].append(1)

def winter():
    # S2D2가 돌아다니면서 땅에 양분을 추가한다.
    for i in range(n):
        for j in range(n):
            # 양분 그래프에 추가해야 하는 양분을 추가해준다.
            food_graph[i][j] += add_graph[i][j]


# 시뮬레이션 진행
for _ in range(k):
    death_pos = spring()
    summer(death_pos)
    autumn()
    winter()

answer = 0
for x in range(n):
    for y in range(n):
        if graph[x][y]:
            answer += len(graph[x][y])
print(answer)