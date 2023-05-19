# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

# 3 x 1 = 0
# 3 x 2 = 3
# 3 x 3 = 0
# 3 x 4 = 11
# 3 x 5 = 0
# 3 x 6 = 41

n = int(input())
dp = [0] * (n + 1)

if n % 2 == 1:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(2, i - 2, 2):
            dp[i] += dp[j] * 2

    print(dp[n])