def solution(n):
    answer = 0
    arr = list(map(int, str(n)))
    arr.sort(reverse=True)
    answer = ''.join(list(map(str, arr)))
    print(answer)
    return int(answer)