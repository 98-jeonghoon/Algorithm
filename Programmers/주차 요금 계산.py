def solution(fees, records):
    import math
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees
    dic = dict()
    for record in records:
        time, num, state = record.split(' ')
        time_minute = int(time[:2]) * 60 + int(time[3:])
        if num not in dic:
            dic[num] = [(time_minute, state)]
        else:
            dic[num].append((time_minute, state))
    dic = list(dic.items())
    dic = sorted(dic, key=lambda x : x[0])
    
    for dics in dic:
        tmp = 0
        for i in dics[1]:
            if i[1] == 'IN':
                tmp -= i[0]
            else:
                tmp += i[0]

        if dics[1][-1][1] == 'IN':
            tmp += 23 * 60 + 59
        
        if tmp <= default_time:
            answer.append(default_fee)
        else:
            answer.append(default_fee + math.ceil((tmp - default_time) / unit_time) * unit_fee)

    return answer
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))