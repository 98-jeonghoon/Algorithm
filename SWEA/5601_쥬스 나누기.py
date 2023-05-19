t = int(input())

for test in range(1, t + 1):
    n = int(input())
    print(f'#{test}',end=' ')
    for i in range(1, n + 1):
        print(f'1/{n}', end=' ')
    print()