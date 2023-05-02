# replace를 이용한 풀이 (야매 풀이)

# arr = ['00', '11', '22', '33', '44', '55', '66', '77','88', '99']
# for test in range(1, 11):
#     n, s = input().split()
#     flag = True

#     while True:
#         if flag == False:
#             break
#         for i in arr:
#             if i in s:
#                 s = s.replace(i, '')
#                 break
#         else:
#             flag = False

#     print('#{} {}'.format(test, s))

# 정석 풀이 , stack을 이용한 풀이

for test in range(1, 11):
    n, s = input().split()
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    answer = ''.join(stack)
    print(f'#{test} {answer}')