n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []

def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(0, len(num)):
        # if num[i] in arr:
        #     continue
        arr.append(num[i])
        backtracking()
        arr.pop()

backtracking()