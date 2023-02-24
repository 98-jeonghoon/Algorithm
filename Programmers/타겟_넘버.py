def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def back_tracking(depth, result):
        if depth == n:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            back_tracking(depth + 1, result + numbers[depth])
            back_tracking(depth + 1, result - numbers[depth])
            
    back_tracking(0, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))