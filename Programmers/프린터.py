def solution(priorities, location):
    from collections import deque
    answer = 0
    arr = []
    for idx, prior in enumerate(priorities):
        arr.append((idx, prior))
    queue = deque(arr)

    while queue:
        max_prior = max(queue, key=lambda x:x[1])[1]
        idx, prior = queue.popleft()
        if queue and prior < max_prior:
            queue.append((idx, prior))
        else:
            answer += 1
            if idx == location:
                break
        
    return answer

print(solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1))
print(solution([2, 1, 3, 2], 2))
print(solution([1,1,9,1,1,1], 0))