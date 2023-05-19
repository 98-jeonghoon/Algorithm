def is_prime(x):
    import math
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(2, 10**6 + 1):
    if is_prime(i):
        print(i, end=' ')