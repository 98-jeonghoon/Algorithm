def solution(n):
    bin_n = bin(n)[2:]
    one_num = bin_n.count('1')
    while True:
        n += 1
        if bin(n)[2:].count('1') == one_num:
            break
    return n