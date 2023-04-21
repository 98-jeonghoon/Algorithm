n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
parent = list(range(n))
plan = list(map(int, input().split()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i, j)

for i in range(1, m):
    if parent[plan[i] - 1] != parent[plan[0] - 1]:
        print('NO')
        break
else:
    print('YES')