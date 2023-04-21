# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# v, e = map(int, input().split())
# parent = [0] * (v + 1)

# for i in range(1, v + 1):
#     parent[i] = i

# for _ in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# # print(parent)
# print('각 원소가 속한 집합: ', end=' ')
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')

# print()
# print('부모 테이블: ', end=' ')
# for i in range(1, v + 1):
#     print(parent[i], end=' ')

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

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

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union_parent(parent, a, b)
    elif command == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
