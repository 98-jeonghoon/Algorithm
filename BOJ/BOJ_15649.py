n, m = map(int, input().split())
arr = []
visited = [False] * (n+1)
def backtracking(start):
    if len(arr) == m:
        print(arr)
        return
        
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        backtracking(i)
        visited[i] = False
        arr.pop()
        
backtracking(1)