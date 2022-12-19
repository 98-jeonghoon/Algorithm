def solution(records):
    answer = []
    dic = {}
    for record in records:
        words = record.split(' ')
        # print(words)
        if len(words) == 3:
            dic[words[1]] = words[2]
    for record in records:
        words = record.split(' ')
        if words[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(dic[words[1]]))
        elif words[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(dic[words[1]]))
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))