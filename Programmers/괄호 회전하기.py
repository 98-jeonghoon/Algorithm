def check(s) -> bool:
    stack = []
    for i in s:
        if stack == []:
            stack.append(i)
        else:
            if stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        return True
    else:
        return False

def solution(s):
    from collections import deque
    answer = 0
    s = deque(s)

    for _ in range(len(s)):
        if check(s):
            answer += 1
        s.rotate(-1)
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))