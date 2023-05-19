# def solution(progresses, speeds):
#     answer = []
#     arr = []
#     for i in range(len(progresses)):
#         count = 0
#         while True:
#             count += 1
#             progresses[i] += speeds[i]
#             if progresses[i] >= 100:
#                 break
#         arr.append(count)
#     from collections import deque
#     queue = deque(arr)
#     while queue:
#         tmp = queue.popleft()
#         cnt = 1
#         while queue and tmp >= queue[0]:
#             queue.popleft()
#             cnt += 1
#         answer.append(cnt)
        
#     return answer

def solution(progresses, speeds):
    from collections import deque
    arr = []
    for i in range(len(progresses)):
        cnt = 0
        while True:
            if progresses[i] >= 100:
                arr.append(cnt)
                break
            cnt += 1
            progresses[i] += speeds[i]
    queue = deque(arr)
    answer = []
    while queue:
        res = 1
        now = queue.popleft()
        while queue and now >= queue[0]:
            queue.popleft()
            res += 1
        answer.append(res)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))