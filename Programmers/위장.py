def solution(clothes):
    answer = 1
    dic = dict()
    for value, key in clothes:
        if key not in dic:
            dic[key] = [value]
        else:
            dic[key].append(value)
            
    arr = list(dic.values())
    for i in arr:
        answer *= len(i) + 1
    return answer - 1