# 상근이가 설탕을 N킬로그램 배달해야됨
# 봉지는 3kg, 5kg 존재
# 배달하는 봉지의 최소 수

n  = int(input())
count = 0

while n >= 0:
    if n % 5 == 0:
        count += (n//5)
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)