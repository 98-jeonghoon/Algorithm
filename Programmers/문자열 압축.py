# def solution(s):
#     result=[]
#     if len(s)==1:
#         return 1
#     for i in range(1, (len(s)//2)+1):
#         b = ''
#         cnt = 1
#         tmp=s[:i]

#         for j in range(i, len(s), i):
#             if tmp==s[j:i+j]:
#                 cnt+=1
#             else:
#                 if cnt!=1:
#                     b = b + str(cnt)+tmp
#                 else:
#                     b = b + tmp
#                 tmp=s[j:j+i]
#                 cnt = 1
#         if cnt!=1:
#             b = b + str(cnt) + tmp
#         else:
#             b = b + tmp
                
#         result.append(len(b))
#     return min(result)

# print(solution("aabbaccc"))


def solution(s):
    answer = 0
    arr = []
    n = len(s) // 2
    for i in range(1, n+1):
        tmp = ''
        count = 1
        compare = s[:i]
        for j in range(i, len(s), i):
            if compare == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    tmp += str(count) + compare
                else:
                    tmp += compare
                compare = s[j:j+i]
                count = 1
        if count != 1:
            tmp += str(count) + compare
        else:
            tmp += compare
        arr.append(len(tmp))
    return min(arr)


    


print(solution("aabbaccc"))