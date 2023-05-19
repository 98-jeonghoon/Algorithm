t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    socre = list(map(int, input().split()))
    socre.sort(reverse=True)
    print(f'#{test} {sum(socre[:k])}')