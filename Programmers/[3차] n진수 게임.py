import string

def convert(num, base) :
    q, r = divmod(num, base)
    number = string.digits+string.ascii_uppercase
    if q == 0 :
        return number[r] 
    else :
        return convert(q, base) + number[r]
    
def solution(n, t, m, p):
    tmp = ''
    answer = ''
    for i in range(0, m*t):
        tmp += (convert(i, n))
    for i in range(p-1, m*t, m):
        answer += tmp[i]
    return answer

# print(solution(16,16,2,1))
# print(solution(2,4,2,1))
# print(solution(16,16,2,2))

# print(convert(0, 16))

print(convert(84, 16))