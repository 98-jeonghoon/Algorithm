# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(1, n+1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs()
#         s.pop()
#         visited[i] = False
            

# n, m = map(int, input().split())
# s = []
# visited = [False] * (n+1)

# dfs()


# def dp_fibo(n):
#     dp = [0] * (n+1)
#     dp[0], dp[1] = 0, 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-2] + dp[i-1]
#     return dp[n]

# dp_fibo(5)

n, m = map(int, input().split())
arr = []
visited = [False] * (n+1)
def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
        
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        backtracking()
        visited[i] = False
        arr.pop()
        
backtracking()