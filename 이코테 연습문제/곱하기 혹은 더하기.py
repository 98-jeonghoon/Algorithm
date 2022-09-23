# 만약 0이나 1이면 더하는게 더 좋다

S = list(input())
result = 0

for i in S:
    if result == 0:
        result += int(i)
    elif int(i) == 0:
        result += int(i)
    elif int(i) == 1:
        result += int(i)
    else:
        result *= int(i)
        
print(result)