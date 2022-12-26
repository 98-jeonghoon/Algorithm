def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x
def solution(w, h):
    return w * h - (w + h - GCD(w, h))


print(solution(8, 12))