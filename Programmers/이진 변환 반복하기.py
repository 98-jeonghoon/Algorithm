def solution(s):
    answer = []
    zero_num = 0
    count = 0
    while True:
        if s == '1':
            break
        count += 1
        zero_num += s.count('0')
        s = (bin(len(s) - s.count('0')))[2:]
        
    return [count, zero_num]