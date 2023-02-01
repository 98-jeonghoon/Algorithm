from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        if is_Valid(s):
            answer += 1
        s.rotate(-1)
    return answer

def is_Valid(s):
    arr = []
    for i in s:
        if arr == []:
            arr.append(i)
        else:
            if i == ')' and arr[-1] == '(':
                arr.pop()
            elif i == ']' and arr[-1] == '[':
                arr.pop()
            elif i == '}' and arr[-1] == '{':
                arr.pop()
            else:
                arr.append(i)
    if arr == []:
        return True
    else:
        return False

print(solution('[](){}'))