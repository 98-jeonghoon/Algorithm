def solution(operations):
    answer = []
    print(operations)
    for i in operations:
        if i[:2] == 'I ':
            answer.append(int(i[2:]))
        elif i == 'D -1':
            try:
                answer.remove(min(answer))
            except:
                pass
        elif i == 'D 1':
            try:
                answer.remove(max(answer))
            except:
                pass
    
    answer.sort(reverse=True)

    if len(answer) == 0:
        return [0, 0]
    if len(answer) >= 3:
        return [max(answer), min(answer)]
    return answer

# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))