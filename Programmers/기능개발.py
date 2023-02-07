def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        count = 0
        while True:
            count += 1
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                break
        arr.append(count)
    from collections import deque
    queue = deque(arr)
    while queue:
        tmp = queue.popleft()
        cnt = 1
        while queue and tmp >= queue[0]:
            queue.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer


print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))