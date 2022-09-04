# n명의 사람, i번사람이 인출하는데 걸리는 시간p(i)=m

n = int(input())
m = list(map(int, input().split()))

total = 0
m.sort()

for i in range(1, n+1):
    total += sum(m[:i])

print(total)