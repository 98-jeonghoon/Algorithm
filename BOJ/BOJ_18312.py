n, k = map(int, input().split())
k = str(k)
count = 0

for i in range(n+1):
    if i < 10:
        h = '0' + str(i)
    else:
        h = str(i)
    for j in range(60):
        if j < 10:
            m = '0' +str(j)
        else:
            m = str(j)
        for o in range(60):
            if o < 10:
                s = 'o' + str(o)
            else:
                s = str(o)
            if k in h + m + s:
                count += 1
                
print(count)