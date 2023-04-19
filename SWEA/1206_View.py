for test in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    answer = 0
    for i in range(2, n - 2):
        max_value = 0
        max_value = max(max_value, building[i - 1], building[i - 2], building[i + 1], building[i + 2])
        if building[i] > max_value:
            answer += building[i] - max_value

    print('#{} {}'.format(test, answer))
