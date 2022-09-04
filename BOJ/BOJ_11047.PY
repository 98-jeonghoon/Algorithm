# 동전은 총 N종류
# 합을 k로 만들려고 한다

n, k = map(int,input().split())
count = 0

coin_types = []
for i in range(1, n+1):
    coin = int(input())
    coin_types.append(coin)

coin_types.sort(reverse=True)

for coin in coin_types:
    count += k // coin
    k = k%coin
    
print(count)