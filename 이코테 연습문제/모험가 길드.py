n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹수
count = 0 # 해당 그룹에 인원수

# 1 2 2 2 3
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
        
print(result)