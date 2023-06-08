for test in range(1, 11):
    n = int(input())
    crypto = list(map(int, input().split()))
    num = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            idx = int(command[i + 1])
            nums = int(command[i + 2])
            for j in range(nums):
                crypto.insert(idx + j, int(command[i + 2 + (j + 1)]))
        else:
            continue
    
    print('#{} {}'.format(test, ' '.join(map(str, crypto[:10]))))
