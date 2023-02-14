from collections import Counter
r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

def calc():
    graph_len = 0
    for i in range(len(graph)):
        counter = [i for i in graph[i] if i != 0]
        counter = Counter(counter).items()
        counter = sorted(counter, key=lambda x: (x[1], x[0]))
        graph[i].clear()
        graph[i] = []
        for x, y in counter:
            graph[i].append(x)
            graph[i].append(y)
        graph_len = max(graph_len, len(graph[i]))
    count = 0
    while count < 100:
        for i in range(len(graph)):
            if len(graph[i]) != graph_len:
                graph[i].append(0)
        count += 1
    for i in range(len(graph)):
        graph[i] = graph[i][:100]

for i in range(101):
    try:
        if graph[r - 1][c - 1] == k:
            print(i)
            break
    except:
        pass
    
    if len(graph) >= len(graph[0]):
        calc()
    else:
        graph = list(zip(*graph))
        calc()
        graph = list(zip(*graph))
else:
    print(-1)