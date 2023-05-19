t = int(input())
from collections import Counter

for test in range(1, t + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            arr.append(i)
    counter = Counter(arr)
    p = int(input())
    bus = []
    for _ in range(p):
        num = int(input())
        bus.append(num)
    print(f'#{test}', end=' ')
    for i in bus:
        print(counter[i],end=' ')
    print()