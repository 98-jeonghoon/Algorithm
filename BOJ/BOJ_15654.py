n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
visited = [False] * (n+1)

def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in num:
        if visited[num.index(i)]:
            continue
        visited[num.index(i)] = True
        arr.append(i)
        backtracking()
        arr.pop()
        visited[num.index(i)] = False

backtracking()