def recursion(n, m, cnt):
    global answer
    if cnt == m:
        return
    answer *= n
    recursion(n, m, cnt + 1)

for i in range(1, 11):
    t = int(input())
    answer = 1
    n, m = map(int,input().split())
    recursion(n, m, 0)
    print('#{} {}'.format(t, answer))