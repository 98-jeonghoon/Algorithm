def fill(graph):
    max_len = -1e9
    for i in graph:
        max_len = max(len(i), max_len)
    for i in range(5):
        if len(graph[i]) != max_len:
            while len(graph[i]) < max_len:
                graph[i].append('*')
    return graph

t = int(input())
for test in range(1, t + 1):
    graph = [list(input()) for _ in range(5)]
    graph = fill(graph)
    # for i in graph:
    #     print(i)
    answer = ''
    for j in range(len(graph[0])):
        for i in range(5):
            if graph[i][j] == '*':
                continue
            answer += graph[i][j]
    print(f'#{test} {answer}')