# from collections import deque

# def solution(queue1, queue2):
#     answer = 0
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     limit = len(queue1) * 3
#     while True:
#         if sum(queue1) > sum(queue2):
#             queue2.append(queue1.popleft())
#             answer += 1
#         elif sum(queue2) > sum(queue1):
#             queue1.append(queue2.popleft())
#             answer += 1
#         else:
#             break
#         if answer == limit:
#             answer = -1
#             break
#     return answer
        

# print(solution([102, 1], [101, 100]))


from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    limit = len(queue1) * 3
    total = sum_1 + sum_2
    if total % 2 != 0:
        return -1
    while True:
        if sum_1 > sum_2:
            now = queue1.popleft()
            queue2.append(now)
            sum_1 -= now
            sum_2 += now
            answer += 1
        elif sum_2 > sum_1:
            now = queue2.popleft()
            queue1.append(now)
            sum_1 += now
            sum_2 -= now
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer
        

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))