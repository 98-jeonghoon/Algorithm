def solution(name, yearning, photo):
    answer = []
    dic = dict()
    for names, yearnings in zip(name, yearning):
        dic[names] = yearnings
    
    for people in photo:
        count = 0
        for peoples in people:
            try:
                if dic[peoples]:
                    count += dic[peoples]
            except:
                pass
        answer.append(count)
    return answer