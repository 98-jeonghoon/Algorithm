t = int(input())

for test in range(1, t + 1):
    n = int(input())
    card = list(input().split())
    arr = []
    for i in range(n // 2):
        now = card.pop()
        arr.append(now)
    arr = arr[::-1]
    print(f'#{test}', end=' ')
    for x, y in zip(card, arr):
        print(x, y, end=' ')
    else:
        if n % 2 == 1:
            print(card[-1])
        else:
            print()