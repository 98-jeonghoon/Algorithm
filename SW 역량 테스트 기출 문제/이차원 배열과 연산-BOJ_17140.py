r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

from collections import Counter

def rc():
    max_len = 0
    len_graph = len(graph)
    for j in range(len_graph):
        arr = [i for i in graph[j] if i != 0]
        arr = Counter(arr).most_common()
        arr = sorted(arr, key = lambda x : (x[1], x[0]))
        graph[j] = []
        for a, b in arr:
            graph[j].append(a)
            graph[j].append(b)
        len_arr = len(arr)
        if max_len < len_arr * 2:
            max_len = len_arr * 2
    for j in range(len_graph):
        for _ in range(max_len - len(graph[j])):
            graph[j].append(0)
        graph[j] = graph[j][:100]

for i in range(101):
    try:
        if graph[r-1][c-1] == k:
            print(i)
            break
    except:
        pass

    if len(graph) < len(graph[0]):
        graph = list(zip(*graph))
        rc()
        graph = list(zip(*graph))
    else:
        rc()
else:
    print(-1)
    