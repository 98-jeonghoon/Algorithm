def solution(numbers, hand):
    answer = ''
    left_arr = [1, 4, 7, '*']
    right_arr = [3, 6, 9, '#']
    mid_arr = [2, 5, 8, 0]
    for i in numbers:
        if i in mid_arr:
            if not answer:
                answer += hand
            else:
                answer += answer[-1]
        elif i in left_arr:
            answer += 'L'
        elif i in right_arr:
            answer += 'R'
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))