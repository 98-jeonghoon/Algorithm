from itertools import combinations

t = int(input())

for test in range(1, t + 1):
    answer = 0
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(len(num) + 1):
        for com in combinations(num, i):
            if sum(com) == k:
                answer += 1
    
    print('#{} {}'.format(test, answer))
