# from collections import deque
# t = int(input())
# for _ in range(t):
#     answer = []
#     commands = list(input())
#     n = int(input())
#     arr = input()
#     if n == 0:
#         print('error')
#         continue
#     arr = arr[1:-1]
#     arr = arr.split(',')
#     arr = [int(i) for i in arr]
#     queue = deque(arr)
#     # print(queue)

#     flag = True
#     for command in commands:
#         if command == 'R':
#             queue.reverse()
#         elif command == 'D':
#             if len(queue) == 0:
#                 flag = False
#                 break
#             else:
#                 queue.popleft()
#     if flag == False:
#         print('error')
#     else:
#         answer += queue
#         print(answer)

from collections import deque

t = int(input())
for _ in range(t):
    commands = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    if n == 0:
        if 'D' in commands:
            print('error')
        else:
            print('[]')
        continue

    arr = [int(i) for i in arr if i]
    queue = deque(arr)

    reverse = False
    error = False

    for command in commands:
        if command == 'R':
            reverse = not reverse
        elif command == 'D':
            if len(queue) == 0:
                error = True
                break
            else:
                if reverse:
                    queue.pop()
                else:
                    queue.popleft()

    if error:
        print('error')
    else:
        if reverse:
            queue.reverse()
        print('[{}]'.format(','.join(map(str, queue))))
