def check(number):
    for n in str(number):
        if int(n) in broken:
            return False
    return True

n = int(input())
m = int(input())
if m == 0:
    broken = []
else:
    broken = list(map(int, input().split()))

min_count = abs(n - 100)

for i in range(1000001):  # 500000에서 모든 숫자를 누를 수 있는 최대 횟수가 6이므로 500000 + 10^6을 고려해야 함
    if check(i):
        count = len(str(i)) + abs(n - i)
        if count < min_count:
            min_count = count

print(min_count)
