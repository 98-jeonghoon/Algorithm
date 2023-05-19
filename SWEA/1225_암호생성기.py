from collections import deque


for test in range(1, 11):
    tc = int(input())
    queue = list(map(int, input().split()))
    queue =deque(queue)

    while True:
        if queue[-1] == 0:
            break
        
        for i in range(1, 6):
            now = queue.popleft()
            now -= i
            if now <= 0:
                now = 0
                queue.append(now)
                break
            queue.append(now)

    print(f'#{tc}',end=' ')
    print(*queue)