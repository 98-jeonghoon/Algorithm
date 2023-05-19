# t = int(input())
# from itertools import combinations

# for test in range(1, t + 1):
#     n, l = map(int, input().split())
#     arr = []
#     for _ in range(n):
#         taste, kcal = map(int, input().split())
#         arr.append((taste, kcal))
    
#     comb = []
#     for i in range(1, len(arr) + 1):
#         for case in combinations(arr, i):
#             comb.append(case)
#     max_value = -1e9
    
#     for i in comb:
#         taste, kcal = 0, 0
#         for j in i:
#             taste += j[0]
#             kcal += j[1]
#         if kcal > l:
#             continue
#         else:
#             max_value = taste
#     print(f'#{test} {max_value}')

# from itertools import combinations

# def find_max_taste(n, l, arr):
#     max_value = 0
#     for i in range(1, n + 1):
#         for case in combinations(arr, i):
#             taste = sum(t for t, k in case)
#             kcal = sum(k for t, k in case)
#             if kcal <= l:
#                 max_value = max(max_value, taste)
#     return max_value

# t = int(input())

# for test in range(1, t + 1):
#     n, l = map(int, input().split())
#     arr = [tuple(map(int, input().split())) for _ in range(n)]
#     result = find_max_taste(n, l, arr)
#     print(f'#{test} {result}')


from itertools import combinations
 
t = int(input())
for tc in range(1, t+1):
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
 
    for i in range(1, n+1):
        for j in combinations(arr, i):
            k_sum = 0
            t_sum = 0
            for k in range(len(j)):
                k_sum += j[k][1]
                t_sum += j[k][0]
 
            if k_sum <= l:
                answer = max(answer, t_sum)
    print(f'#{tc} {answer}')