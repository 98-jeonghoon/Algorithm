#잡화점 잔돈 500, 100, 50, 10, 5, 1
# 거스름돈 개수가 가장 작게 돌려준다

price = int(input())
pay = 1000
change = pay - price
count = 0

coin_types = [500, 100, 50, 10, 5, 1]
for coin in coin_types:
    count += change//coin
    change %= coin
print(count)