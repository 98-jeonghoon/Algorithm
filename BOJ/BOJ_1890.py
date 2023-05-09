n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n -1 and j == n - 1:
            print(dp[i][j])
            exit(0)
        move = graph[i][j]
        if 0 <= i + move < n: 
            dp[i + move][j] += dp[i][j]
        if 0 <= j + move < n:
            dp[i][j + move] += dp[i][j]

for i in dp:
    print(i)