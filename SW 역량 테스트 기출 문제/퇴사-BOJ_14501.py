n = int(input())
graph = []
for i in range(n):
    a, b = map(int, input().split())
    graph.append([a, b])

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if i + graph[i][0] > n :
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], graph[i][1] + dp[i + graph[i][0]])

print(dp[0])