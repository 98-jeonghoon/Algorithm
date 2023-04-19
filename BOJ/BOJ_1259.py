def check(s):
    if s == s[::-1]:
        return True
    return False

while True:
    s = int(input())
    if s == 0:
        break
    if check(str(s)):
        print('yes')
    else:
        print('no')