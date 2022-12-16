def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        first = heapq.heappop(scoville)
        if first < K:
            second = heapq.heappop(scoville)
            mix = first + (second * 2)
            heapq.heappush(scoville, mix)
            answer += 1

        else:
            return answer
    
    
print(solution([1, 2, 3, 9, 10, 12], 7))