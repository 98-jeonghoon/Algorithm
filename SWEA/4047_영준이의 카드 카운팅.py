t = int(input())
for test in range(1, t + 1):
    s = input()
    sp, di, he, cl = [], [], [], []
    flag = True
    for i in range(len(s)):
        if s[i].isalpha():
            res = s[i+1] + s[i+2]
            if s[i] == 'S':
                if res in sp:
                    flag = False
                    break
                else:
                    sp.append(res)
            elif s[i] == 'D':
                if res in di:
                    flag = False
                    break
                else:
                    di.append(res)
            elif s[i] == 'H':
                if res in he:
                    flag = False
                    break
                else:
                    he.append(res)
            elif s[i] == 'C':
                if res in cl:
                    flag = False
                    break
                else:
                    cl.append(res)
    if flag == False:
        print(f'#{test} ERROR')
    else:
        a, b, c, d = 13 - len(sp), 13 - len(di), 13 - len(he), 13 - len(cl)
        print(f'#{test} {a} {b} {c} {d}')

            
    