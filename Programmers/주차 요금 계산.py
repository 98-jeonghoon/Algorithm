def solution(fees, records):
    answer = []
    dic = {}
    for record in records:
        time, car_num, history = record.split(' ')
        time_minute = int(time[:2]) * 60 + int(time[3:])
        if history == 'IN':
            dic[car_num] = time_minute
        else:
            duration = time_minute - dic[car_num]
            if duration <= fees[0]:
                fee = fees[1]
            else:
                fee = fees[1] + (duration - fees[0]) // fees[2] * fees[3]
            dic[car_num] = fee
    dic = sorted(dic.items(), key = lambda x: x[0])
    return [fee for _, fee in dic]


print(solution([180, 5000, 10, 600] , 
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
                "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))