def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def check_f(s, t):
    if s * len(t) == t * len(s):
        return True
    return False

T = int(input())

for test in range(1, T + 1):
    s, t = input().split()
    lcm = len(s) * len(t) // gcd(len(s), len(t))
    s = s * (lcm // len(s))
    t = t * (lcm // len(t))
    
    if check_f(s, t):
        print(f'#{test} yes')
    else:
        print(f'#{test} no')
