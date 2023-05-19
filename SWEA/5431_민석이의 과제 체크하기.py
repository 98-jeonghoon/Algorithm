t = int(input())

for test in range(1, t + 1):
    n, m = map(int, input().split())
    non = list(map(int, input().split()))
    peoeple = [i for i in range(1, n + 1) if i not in non]
    print('#{}'.format(test), end=' ')
    print(*peoeple)