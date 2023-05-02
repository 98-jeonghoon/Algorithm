from collections import deque
t = int(input())
for test in range(1, t + 1):
    k = int(input())
    queue = list(map(int, input().split()))
    queue = deque(queue)
    answer = 0
    while len(queue) != 1:
        first, second = queue.popleft(), queue.popleft()
        max_value = max(first, second)
        min_Value = min(first, second)
        answer += max_value - min_Value
        queue.append(max_value)
    print(f'#{test} {answer}')