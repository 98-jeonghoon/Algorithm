def solution(plans):
    plans.sort(key = lambda x : x[1])
    wait = []
    answer = []
    
    for subject, time, during in plans:
        hour, minutes = time.split(':')
        time = 60 * int(hour) + int(minutes)
        during = int(during)
        
        if wait:
            prev_subject, prev_time, prev_during = wait.pop()
            extra_time = time - prev_time
            if extra_time < prev_during:
                wait.append((prev_subject, prev_time, prev_during - extra_time))
            else:
                answer.append(prev_subject)
                extra_time -= prev_during
                
                while wait and extra_time:
                    prev_subject, prev_time, prev_during = wait.pop()
                    
                    if extra_time < prev_during:
                        wait.append((prev_subject, prev_time, prev_during - extra_time))
                        break
                    else:
                        answer.append(prev_subject)
                        extra_time -= prev_during
        wait.append((subject, time, during))
    
    for i in wait[::-1]:
        answer.append(i[0])   
    return answer
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
