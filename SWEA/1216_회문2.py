for test in range(1, 11):
    n = 100
    tc = int(input())
    graph = []
    for _ in range(n):
        graph.append(input())

    def check(s):
        if s == s[::-1]:
            return True
        return False

    arr = []
    for i in graph:
        for j in range(len(i)):
            for k in range(j + 1, len(i) + 1):
                if check(i[j:k]):
                    arr.append(i[j:k])
    graph = list(map(list, zip(*graph[::-1])))

    for i in graph:
        for j in range(len(i)):
            for k in range(j + 1, len(i) + 1):
                if check(i[j:k]):
                    arr.append(i[j:k])

    answer = -1e9

    for i in arr:
        answer = max(answer, len(i))

    print('#{} {}'.format(test, answer))