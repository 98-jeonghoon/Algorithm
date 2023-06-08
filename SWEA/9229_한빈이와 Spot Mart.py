from itertools import combinations
t = int(input())

for test in range(1, t + 1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    max_value = -1e9
    for x, y in combinations(weight, 2):
        if x + y > m:
            continue
        else:
            max_value = max(max_value, x + y)
    if max_value == -1e9:
        max_value = -1
    
    print('#{} {}'.format(test, max_value))