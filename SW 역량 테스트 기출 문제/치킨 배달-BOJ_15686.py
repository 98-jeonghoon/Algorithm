## 백트래킹 문제풀이
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# house = []
# chicken = []

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 2:
#             chicken.append((i, j))
#         elif graph[i][j] == 1:
#             house.append((i, j))

# visited = [False] * (len(chicken) + 1)
# answer = 1e9

# def dfs(depth, idx):
#     global answer
#     if depth == m:
#         total_distance = 0
#         for house_x, house_y in house:
#             distance = 1e9
#             for i, loc in enumerate(chicken):
#                 if visited[i]:
#                     chicken_x, chicken_y = loc
#                     distance = min(distance, abs(house_x - chicken_x) + abs(house_y - chicken_y))
#             total_distance += distance
#         answer = min(answer, total_distance)
#         return
    
#     for i in range(idx, len(chicken)):
#         visited[i] = True
#         dfs(depth + 1, i + 1)
#         visited[i] = False

# dfs(0, 0)

# print(answer)
    
## combination(조합 사용) 문제 풀이
from itertools import combinations
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))
            
answer = 1e9

for comb in combinations(chicken, m):
    total_distance = 0
    for house_x, house_y in house:
        distance = 1e9
        for chicken_x, chicken_y in comb:
            distance = min(distance, abs(house_x - chicken_x) + abs(house_y - chicken_y))
        total_distance += distance
    answer = min(answer, total_distance)
            
print(answer)