def solution(s):
    answer = 0
    arr = []
    n = len(s) // 2
    for i in range(1, n+1):
        tmp = ''
        count = 1
        compare = s[:i]
        for j in range(i, len(s), i):
            if compare == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    tmp += str(count) + compare
                else:
                    tmp += compare
                compare = s[j:j+i]
                count = 1
        if count != 1:
            tmp += str(count) + compare
        else:
            tmp += compare
        arr.append(len(tmp))
    return min(arr)


    


print(solution("aabbaccc"))