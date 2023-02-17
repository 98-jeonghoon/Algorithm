def solution(n, k):
    from itertools import permutations
    answer = []
    arr = [i for i in range(1, n+1)]
    for idx, i in enumerate(permutations(arr, n), start=1):
        if idx == k:
            answer.append(''.join(map(str,i)))
    return list(map(int,answer[-1]))

print(solution(3, 5))