def solution(lottos, win_nums):
    answer = []
    arr = []
    _intersection = list(set(lottos) & set(win_nums))
    zero_num = lottos.count(0)
    arr.append(len(_intersection) + zero_num)
    arr.append(len(_intersection))
    for count in arr:
        if count == 6:
            answer.append(1)
        elif count == 5:
            answer.append(2)
        elif count == 4:
            answer.append(3)
        elif count == 3:
            answer.append(4)
        elif count == 2:
            answer.append(5)
        else:
            answer.append(6)
    answer.sort()
    return answer
    
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# if count == 6:
# answer.append(1)
# elif count == 5:
# answer.append(2)
# elif count == 4:
# answer.append(3)
# elif count == 3:
# answer.append(4)
# elif count == 2:
# answer.append(5)
# else:
# answer.append(6)