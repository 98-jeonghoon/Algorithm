def solution(n, s):
    if n > s:
        return [-1]
    
    p, q = divmod(s, n)
    answer = [p] * n

    for i in range(q):
        answer[i] += 1
    
    answer.sort()
    return answer