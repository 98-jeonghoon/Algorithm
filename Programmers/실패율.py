def solution(N, stages):
    answer = []
    dic = {}
    people = len(stages)
    for i in range(1, N+1):
        if people != 0:
            fail_rate = stages.count(i) / people
            people -= stages.count(i)
            dic[i] = fail_rate
        else:
            dic[i] = 0
    # for i in range(N):
        # answer.append(dic.keys(min(dic.values)))
    
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for i in dic:
        if i[0] > N:
            continue
        answer.append(i[0])
        
    
    return answer

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))