def solution(sequence, k):
    answer = []
    n = len(sequence)
    interval_sum, end = 0,0
    
    for i in range(n):
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end +=1
            
        if interval_sum == k:
            answer.append([i, end-1, end-1-i])
        
        interval_sum -= sequence[i]
        
    answer = sorted(answer, key=lambda x: x[2])
    
    return answer[0][:2]

solution([1, 1, 1, 2, 3, 4, 5], 5)