import string

t = int(input())
for test in range(t):
    arr = list(string.ascii_lowercase)
    alpha = list(input())
    count = 0
    for i in range(len(alpha)):
        if alpha[i] == arr[i]:
            count += 1
        else:
            break
    print('#{} {}'.format(test+1, count))

