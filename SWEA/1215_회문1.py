for test in range(1, 11):
    n = 8
    num = int(input())
    graph = [list(input()) for _ in range(8)]

    def check(s):
        if s == s[::-1] and len(s) == num:
            return True
        return False

    arr = []
    for i in range(n):
        for j in range(n - num + 1):
            s = ''
            for k in range(num):
                s += graph[i][j + k]
                arr.append(s)

    graph = list(map(list, zip(*graph[::-1])))

    for i in range(n):
        for j in range(n - num + 1):
            s = ''
            for k in range(num):
                s += graph[i][j + k]
                arr.append(s)

    answer = 0

    for i in arr:
        if check(i):
            answer += 1

    print('#{} {}'.format(test, answer))