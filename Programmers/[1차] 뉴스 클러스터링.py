def solution(str1, str2):
    from collections import Counter
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    # str1 = str1.replace(' ','')
    # str2 = str2.replace(' ','')
    arr1, arr2 = [], []
    for i in range(0, len(str1) -1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i]+str1[i+1])
    for j in range(0, len(str2) - 1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            arr2.append(str2[j] + str2[j+1])
    len_inter = sum((Counter(arr1) & Counter(arr2)).values())
    len_union = sum((Counter(arr1) | Counter(arr2)).values())

    if len_inter == 0 and len_union == 0:
        return 65536
    else:
        return int(len_inter / len_union * 65536)

print(solution('FRANCE', 'french'))