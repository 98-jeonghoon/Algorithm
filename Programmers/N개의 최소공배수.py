def solution(arr):
    from math import gcd
    answer = 1
    for num in arr:
        answer = answer * num // gcd(answer, num)
    return answer