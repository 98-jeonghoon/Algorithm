def sep(s):
    a, b = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            a += 1
        else:
            b += 1
        if a == b:
            u = s[:i+1]
            v = s[i+1:]
            return u, v

def check_collect(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ''
    if not p:
        return ''
    u, v = sep(p)

    if check_collect(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('

        return answer