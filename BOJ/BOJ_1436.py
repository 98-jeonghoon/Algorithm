def find_title_number(n):
    count = 0
    num = 665
    while count < n:
        num += 1
        if '666' in str(num):
            count += 1
    return num

N = int(input())
print(find_title_number(N))
