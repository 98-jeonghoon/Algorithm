def solution(priorities, location):
    from collections import deque
    queue = deque([(p, idx) for idx, p in enumerate(priorities)])
    answer = 0
    while queue:
        job = queue.popleft()
        if queue and job[0] < max(queue)[0]:
            queue.append(job)
        else:
            answer += 1
            if job[1] == location:
                break

    return answer

print(solution([2,1,3,2], 2))