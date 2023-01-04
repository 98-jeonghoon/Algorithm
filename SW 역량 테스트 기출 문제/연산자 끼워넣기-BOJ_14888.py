<<<<<<< HEAD
# import copy
# N = int(input())
# num = list(map(int, input().split()))
# num1 = copy.deepcopy(num)
# sum, sub, mul, div = map(int, input().split())
# num.sort()
# num1.sort()
# max_num = num.pop(0)
# min_num = num1.pop(0)

# def min_value(num1, sum, sub, mul, div, min_num):
#     while True:
#         if len(num1) == 0:
#             break
#         if sum == 0 and sub == 0 and mul == 0 and div == 0:
#             break
#         if sum >= 1:
#             sum -= 1
#             min_num += num1.pop(0)
#         elif div >= 1:
#             div -= 1
#             if min_num < 0:
#                 min_num = abs(min_num) // num1.pop(0)
#                 min_num *= -1
#             else:
#                 min_num = min_num // num1.pop(0)
#         elif sub >= 1:
#             sub -= 1
#             min_num -= num1.pop(0)
#         elif mul >= 1:
#             mul -= 1
#             min_num *= num1.pop(0)
#     return min_num

# def max_value(num, sum, sub, mul, div, max_num):
#     while True:
#         if len(num) == 0:
#             break
#         if sum == 0 and sub == 0 and mul == 0 and div == 0:
#             break
#         if sub >= 1:
#             sub -= 1
#             max_num -= num.pop(0)
#         elif div >= 1:
#             div -= 1
#             if max_num < 0:
#                 max_num = abs(max_num) // num.pop(0)
#                 max_num *= -1
#             else:
#                 max_num = max_num // num.pop(0)
#         elif sum >= 1:
#             sum -= 1
#             max_num += num.pop(0)
#         elif mul >= 1:
#             mul -= 1
#             max_num *= num.pop(0)
#     return max_num

# print(max_value(num, sum, sub, mul, div, max_num))
# print(min_value(num1,sum, sub, mul, div, min_num))

# from itertools import permutations

# N = int(input())
# num = list(map(int, input().split()))
# operator = list(map(int, input().split()))
# operator_list = ['+', '-', '*', '/']
# arr = []

# for i in range(len(operator)):
#     for j in range(operator[i]):
#         arr.append(operator_list[i])

# max_num = -1e9
# min_num = 1e9

# def solution(max_num, min_num):
#     for case in permutations(arr, N-1):
#         answer = num[0]
#         for i in range(1, N):
#             if case[i - 1] == '+':
#                 answer += num[i]
#             elif case[i - 1] == '-':
#                 answer -= num[i]
#             elif case[i - 1] == '*':
#                 answer *= num[i]
#             elif case[i - 1] == '/':
#                 answer = int(answer / num[i])
#         if answer > max_num:
#             max_num = answer
#         if answer < min_num:
#             min_num = answer
#     print(max_num)
#     print(min_num)
    
# solution(max_num, min_num)

N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

total = num[0]
max_num = -1e9
min_num = 1e9

def calc(depth, total, add, sub, mul, div):
    global max_num, min_num
    if depth == N:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return
    if add:
        calc(depth+1, total + num[depth], add-1, sub, mul, div)
    if sub:
        calc(depth+1, total - num[depth], add, sub-1, mul, div)
    if mul:
        calc(depth+1, total * num[depth], add, sub, mul - 1, div)
    if div:
        calc(depth+1, int(total / num[depth]), add, sub, mul, div - 1)

calc(1, total, add, sub, mul, div)
print(max_num)
print(min_num)

