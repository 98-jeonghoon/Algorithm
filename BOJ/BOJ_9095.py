t = int(input())

# def dynamic_programing(n):
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4
#     for i in range(4, n + 1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#     return dp[-1]

for i in range(t):
    n = int(input())
    dp = [0] * (n + 1)
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp[1], dp[2], dp[3] = 1, 2, 4
        for j in range(4, n+1):
            dp[j] = dp[j-1] + dp[j - 2] + dp[j -3]
        print(dp[-1])