t = int(input())

for test in range(1, t + 1):
    board, n = input().split()
    n = int(n)
    now = set([board])
    nxt = set()
    
    for _ in range(n):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(len(board) - 1):
                for j in range(i + 1, len(board)):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now
    
    answer = max(map(int, now))
    print(f'#{test} {answer}')