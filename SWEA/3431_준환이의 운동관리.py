t = int(input())
for test in range(1, t + 1):
    l, u, x = map(int, input().split())
    answer = 0
    if l <= x <= u:
        answer = 0
    else:
        if x > u:
            answer = -1
        else:
            answer = l - x

    print(f'#{test} {answer}')