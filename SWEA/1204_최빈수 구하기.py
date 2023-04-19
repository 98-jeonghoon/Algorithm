t = int(input())
for _ in range(t):
    from collections import Counter
    n = int(input())
    student = list(map(int, input().split()))
    count = Counter(student)
    count = list(count.items())
    count.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print('#{} {}'.format(n, count[0][0]))