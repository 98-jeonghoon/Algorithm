def solution(dartResult):
    arr = []
    answer = ''
    for i in dartResult:
        if i.isdigit():
            answer += i
        elif i == 'S':
            answer = int(answer) ** 1
            arr.append(answer)
            answer = ''
        elif i == 'D':
            answer = int(answer) ** 2
            arr.append(answer)
            answer = ''
        elif i =='T':
            answer = int(answer) ** 3
            arr.append(answer)
            answer = ''
        elif i == '*':
            star_count += 1
            if star_count >= 3:
                continue
            if len(arr) > 1:
                arr[-1] = arr[-1] * 2
                arr[-2] = arr[-2] * 2
            else:
                arr[-1] = arr[-1] * 2
        elif i == '#':
            arr[-1] = arr[-1] * -1
    return sum(arr)

print(solution('1S*2D*3T*'))