import heapq

n = int(input())
queue = []
arr = []
for _ in range(n):
    num = -int(input())
    if num == 0:
        if queue == []:
            arr.append(0)
        else:
            arr.append(abs(queue[0]))
            heapq.heappop(queue)
    else:
        heapq.heappush(queue, num)

for i in arr:
    print(i)