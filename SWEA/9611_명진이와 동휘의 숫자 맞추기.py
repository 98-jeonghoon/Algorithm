t = int(input())
for test in range(t):
    n = int(input())
    arr = []
    answer = []
    no_arr = []
    ok_arr = []
    for _ in range(n):
        arr.append(list(input().split()))

    for i in range(len(arr)):
        if arr[i][-1] == 'NO':
            no_arr += arr[i][:-1]
        else:
            ok_arr += arr[i][:-1]

    for i in ok_arr:
        if i in no_arr:
            continue
        else:
            answer.append(i)
    print('#{}'.format(test + 1), end=' ')
    print(*answer)