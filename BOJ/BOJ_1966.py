from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    printer = list(map(int, input().split()))
    queue = deque()

    for idx, prior in enumerate(printer):
        queue.append((idx, prior))

    answer = 0 
    while queue:
        max_value = max(queue, key=lambda x : x[1])[1]
        idx, prior = queue.popleft()
        if queue and prior < max_value:
            queue.append((idx, prior))
        else:
            answer += 1
            if idx == m:
                break
    print(answer)
    