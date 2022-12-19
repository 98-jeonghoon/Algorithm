def solution(numbers):
    from itertools import permutations
    import math
    answer = 0
    numbers = list(numbers)
    arr = []
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            arr.append(''.join(j))
    def is_prime_number(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    arr = list(set(list(map(int, arr))))
    print(arr)
    for i in arr:
        if i == 1:
            continue
        if is_prime_number(i):
            answer += 1
    return answer

print(solution('011'))