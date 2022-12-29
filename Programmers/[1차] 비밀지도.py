def solution(n, arr1, arr2):
    answer = []
    set_arr1 = []
    set_arr2 = []
    for i in range(n):
        set_arr1.append(bin(arr1[i])[2:])
        set_arr2.append(bin(arr2[i])[2:])
        
    for i in range(n):
        answer.append(int(set_arr1[i]) + int(set_arr2[i]))
        while True:
            if len(str(answer[i])) < n:
                answer[i] = '0' + str(answer[i])
            else:
                break
    for i in range(n):
        if '2' in str(answer[i]):
            answer[i] = str(answer[i]).replace('2','1')
        if '1' in str(answer[i]):
            answer[i] = str(answer[i]).replace('1','#')
        if '0' in str(answer[i]):
            answer[i] = str(answer[i]).replace('0',' ')    
                   
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))