import string
def solution(s):
    answer = []
    stack = ''
    for idx, word in enumerate(s):
        if word not in stack:
            stack += word
            answer.append(-1)
        else:
            answer.append(idx - int(stack.rfind(word)))
            stack += word

    return answer


print(solution('banana'))