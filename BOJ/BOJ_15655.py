n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []

def backtracking(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, len(num)):
        if num[i] in arr:
            continue
        arr.append(num[i])
        backtracking(i+1)
        arr.pop()

backtracking(0)

