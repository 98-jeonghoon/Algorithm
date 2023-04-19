n = int(input())

num = 1
for i in range(n, 0, -1):
    num *= i

cnt = 0
for x in str(num)[::-1]:
    if x != '0':
        break
    cnt += 1

print(cnt)