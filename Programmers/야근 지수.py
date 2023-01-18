def solution(works, n):
    import heapq
    answer = 0
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)
    while n > 0:
        value = heapq.heappop(works)
        heapq.heappush(works, value + 1)
        n -= 1
    
    for work in works:
        answer += (work ** 2)
    return answer

print(solution([4,3,3], 4))
# print(solution([2,1,2], 1))
# print(solution([1,1], 3))