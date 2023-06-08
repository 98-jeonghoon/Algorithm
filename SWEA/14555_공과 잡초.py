t = int(input())

for test in range(1, t + 1):
    s = input()
    idx = 0
    answer = 0
    while idx < len(s):
        if s[idx] == '(':
            if s[idx + 1] == ')':
                answer += 1
                idx += 1
            else:
                answer += 1
        elif s[idx] == ')':
            answer += 1
        idx += 1
    
    print(f"#{test} {answer}")