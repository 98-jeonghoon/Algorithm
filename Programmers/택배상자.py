def solution(order):
    answer = 0
    idx = 1
    stack = []
    while idx != len(order) + 1:
        stack.append(idx)
        while stack and stack[-1] == order[answer]:
            answer += 1
            stack.pop()
        idx += 1
    return answer

print(solution([4, 3, 1, 2, 5]))