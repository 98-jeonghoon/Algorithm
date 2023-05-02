from itertools import combinations

t = int(input())

def check(s):
    s = str(s)
    for i in range(len(s) - 1):
        if s[i] <= s[i + 1]:
            continue
        else:
            return False
    return True

for test in range(1, t + 1):
    n = int(input())
    arr = []
    num = list(map(int, input().split()))
    for x, y in combinations(num, 2):
        arr.append(x * y)
    
    answer = 0
    for i in arr:
        if check(i):
            answer = max(answer, i)
    if answer == 0:
        answer = -1
    
    print(f'#{test} {answer}')    