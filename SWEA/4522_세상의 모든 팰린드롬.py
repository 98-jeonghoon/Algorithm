for tc in range(int(input())):
    s = list(input())
    answer=''
    if s == s[::-1]:
        answer = 'Exist'
    else:
        for i in range(len(s)):
            if s[i]=='?':
                s[i]=s[len(s)-(i+1)]
            if s == s[::-1]:
                answer = 'Exist'
            else: answer = 'Not exist'

    print(f'#{tc+1} {answer}')