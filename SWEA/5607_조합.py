def power(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        b //= 2
        a = (a * a) % mod
    return result

def mod_inverse(n, mod):
    return power(n, mod - 2, mod)

def nCr(n, r, mod):
    if r == 0 or r == n:
        return 1
    numerator = 1
    for i in range(n, n - r, -1):
        numerator = (numerator * i) % mod
    denominator = 1
    for i in range(1, r + 1):
        denominator = (denominator * i) % mod
    return (numerator * mod_inverse(denominator, mod)) % mod

t = int(input())
mod = 1234567891

for test in range(1, t + 1):
    n, r = map(int, input().split())
    result = nCr(n, r, mod)
    print(f'#{test} {result}')
