n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []
def backtracking(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n+1):
        # if visited[i]:
        #     continue
        visited[i] = True
        arr.append(i)
        backtracking(i)
        arr.pop()
        visited[i] = False

backtracking(1)