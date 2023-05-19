t = int(input())
for test in range(1, t + 1):
    n, d = map(int, input().split())
    d = d * 2 + 1
    answer = n // d
    if n % d != 0:
        answer += 1
    print(f'#{test} {answer}')
