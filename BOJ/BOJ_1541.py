s = input().split('-')
num = []

for i in s:
    cnt = 0
    add = i.split('+')
    for j in add:
        cnt += int(j)
    num.append(cnt)
n = num[0]

for i in range(1, len(num)):
    n -= num[i]
print(n)