def solution(prices):
    from collections import deque
    queue = deque(prices)
    answer = []
    while queue:
        count = 0
        now = queue.popleft()
        for i in queue:
            count += 1
            if now > i:
                break
        answer.append(count)
    return answer

print(solution([1, 2, 3, 2, 3]))
