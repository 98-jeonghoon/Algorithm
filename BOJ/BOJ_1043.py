n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]
parent = [i for i in range(n + 1)]
for person in truth:
    parent[person] = 0

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

parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party) - 1):
        union_parent(parent, party[i], party[i + 1])
    parties.append(party)

answer = 0
for party in parties:
    for i in party:
        if find_parent(parent, parent[i]) == 0:
            break
    else:
        answer += 1
print(answer)
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

# for i in range(1, v+1):
#     parent[i] = i

# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# print('각 원소가 속한 집합 ',end=' ')
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')

# print()

# print('부모 테이블: ',end=' ')
# for i in range(1, v + 1):
#     print(parent[i], end=' ')