n, m = map(int, input().split())

def is_prime(x):
    import math
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for x in range(n, m + 1):
    if x == 1:
        continue
    if is_prime(x):
        print(x)

