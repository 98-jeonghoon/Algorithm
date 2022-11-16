n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []
def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        # if visited[i]:
        #     continue
        # visited[i] = True
        arr.append(i)
        backtracking()
        arr.pop()
        # visited[i] = False

backtracking()