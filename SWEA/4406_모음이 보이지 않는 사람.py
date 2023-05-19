t = int(input())

for test in range(1, t + 1):
    arr = ['a', 'e', 'i', 'o', 'u']
    s = input()
    answer = ''
    for i in s:
        if i in arr:
            continue
        else:
            answer += i
    print(f'#{test} {answer}')