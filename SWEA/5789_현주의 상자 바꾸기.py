t = int(input())
for test in range(1, t + 1):
    n, q = map(int, input().split())
    num = [0 for _ in range(n)]
    for check in range(1, q + 1):
        left, right = map(int, input().split())
        for i in range(left, right + 1):
            num[i - 1] = check
    print('#{}'.format(test), end=' ')
    for i in num:
        print(i, end=' ')