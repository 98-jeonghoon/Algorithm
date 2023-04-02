def solution(weights):
    from collections import Counter
    
    answer = 0
    counter = Counter(weights)
    
    for k, v in counter.items():
        if v >= 2:
            answer += v * (v - 1) // 2
    weights = list(set(weights))
    for weight in weights:
        for check in (2/3, 2/4, 3/4):
            if weight * check in weights:
                answer += counter[weight] * counter[weight * check]
    
    
    return answer