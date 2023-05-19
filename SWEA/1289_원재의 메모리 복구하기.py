t = int(input())

for test in range(1, t + 1):
    s = list(input())
    s = list(map(int, s))
    arr = [0] * len(s)
    answer = 0
    while arr != s:
        answer += 1
        for i in range(len(s)):
            if s[i] != arr[i]:
                idx = i
                while True:
                    if idx >= len(s):
                        break
                    arr[idx] = s[i]
                    idx += 1
                break
    print(answer)
                    