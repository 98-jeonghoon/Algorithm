def is_prime(x):
    import math
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in arr:
    if i == 1:
        continue
    if is_prime(i):
        answer += 1
        
print(answer)