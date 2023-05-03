from collections import Counter

t = int(input())
for test in range(1, t + 1):
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    counter = list(counter.items())
    counter.sort(key=lambda x : x[1])
    print(f'#{test} {counter[0][0]}')