from itertools import combinations
t = int(input())
for test in range(1, t + 1):
    arr = []
    num = list(map(int, input().split()))
    
    for i in combinations(num, 3):
        arr.append(sum(i))
    arr = list(set(arr))
    arr.sort()
    print(f'#{test} {arr[-5]}')