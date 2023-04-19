s = input()

count = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        continue
    else:
        count +=1

if count == 0 or count == 1:
    print(count)
else:
    count = (count + 1) // 2
    print(count)
    
