def solution(n, stations, w):
    import math
    answer = 0
    W = w * 2 + 1
    start = 1
    for s in stations:
        answer += max(math.ceil((s - w - start) / W), 0)
        start = s + w + 1
    if n >= start:
        answer += math.ceil((n - start + 1) / W)
    
    return answer

print(solution(11, [4,11], 1))
# print(solution(16,[9],2))