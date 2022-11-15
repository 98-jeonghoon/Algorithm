n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
visited = [False] * (n+1)

def backtracking(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    overlap = 0
    for i in range(0, n):
        if overlap != num[i]:
            # visited[i] = True
            arr.append(num[i])
            overlap = num[i]
            backtracking(i)
            # visited[i] = False
            arr.pop()

backtracking(0)