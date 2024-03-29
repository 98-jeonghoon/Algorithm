# n, c = map(int, input().split())
# arr = []
# for _ in range(n):
#     a = int(input())
#     arr.append(a)
# arr.sort()

# start = 1
# end = arr[-1] - arr[0]
# answer = 0
# def binary_search(arr, start, end):
#     global answer
#     while start <= end:
#         mid = (start + end) // 2
#         current = arr[0]
#         count = 1
#         for i in range(1, len(arr)):
#             if arr[i] >= current + mid:
#                 count += 1
#                 current = arr[i]
        
#         if count >= c:
#             start = mid + 1
#             answer = mid
#         else:
#             end = mid - 1
            
# binary_search(arr, start, end)
# print(answer)

# t = int(input())
# for test in range(1, t + 1):
#     s = input()
#     # len_ = len(s)
#     lose_cnt = s.count('x')
#     answer = ''

#     if lose_cnt >= 8:
#         answer = 'NO'
#     else:
#         answer = 'YES'
    
#     print(f'#{test} {answer}')

import string

upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)

def is_name(word):
    # 첫번째 글자
    start = word[0]
    # 나머지 글자
    end = word[1:]
    # 첫번째가 대문자가 아니라면 False를 리턴
    if start not in upper_case:
        return False
    for i in end:
        # 만약 소문자가 아니라면 False를 리턴
        if i not in lower_case:
            return False
    # 모두 통과한다면 True를 리턴
    return True

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    s = input()
    tmp = []
    check_idx = 0
    for i in range(len(s)):
        if s[i] == '!' or s[i] == '.' or s[i] == '?':
            tmp.append(s[check_idx:i])
            check_idx = i + 2
    
    answer = [0] * len(tmp)

    for idx in range(len(tmp)):
        word_arr = tmp[idx].split(' ')
        cnt = 0
        for word in word_arr:
            if is_name(word):
                cnt += 1
        answer[idx] = cnt
    
    print(f'#{test} ', end='')
    print(*answer)
        