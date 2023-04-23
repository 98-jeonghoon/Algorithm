
n = int(input())

a, b, c = map(int, input().split())
max_dp = [a,b,c]
min_dp = [a,b,c]

for i in range(1, n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_first =  max(max_dp[j], max_dp[j+1]) + a
            min_first =  min(min_dp[j], min_dp[j+1]) + a
        if j == 1:
            max_second = max(max_dp[j-1], max_dp[j], max_dp[j+1]) + b
            min_second = min(min_dp[j-1], min_dp[j], min_dp[j+1]) + b
        if j == 2:
            max_third = max(max_dp[j-1], max_dp[j]) + c
            min_third = min(min_dp[j-1], min_dp[j]) + c
    max_dp = [max_first, max_second, max_third]
    min_dp = [min_first, min_second, min_third]
    
print(max(max_dp), min(min_dp))