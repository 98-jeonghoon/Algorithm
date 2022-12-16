def convert_num(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev_base = (rev_base[::-1])
    return rev_base

def is_prime_num(x):
    import math
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = convert_num(n, k)
    num = num.split('0')
    for x in num:
        if x != '' and is_prime_num(int(x)):
            answer += 1
    return answer

print(solution(437674, 3))
