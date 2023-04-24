t = int(input())

for test in range(1, t + 1):
    a, b, c = map(int, input().split())
    min_value = min(a, b)
    print(f'#{test} {c // min_value}')