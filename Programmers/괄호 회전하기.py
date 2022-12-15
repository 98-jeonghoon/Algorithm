def isValid(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif c == ')' or c == ']' or c == '}':
            if not stack or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
                return False
            stack.pop()
    return not stack

def solution(s):
    answer = 0
    for i in range(len(s)):
        word = s[i:] + s[:i]
        if isValid(word):
            answer += 1
    return answer