def solution(s):
    arr = []
    for i in s:
        if arr == []:
            arr.append(i)
        else:
            if i == arr[-1]:
                arr.pop()
            else:
                arr.append(i)
    if arr == []:
        return 1
    else:
        return 0


print(solution('cdcd'))