from numpy import sort


# m =더해지는 횟수, n = 배열크기, k = 초과하면 안되는 수
n , m , k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

# print(sort)
first = data[-1]
second = data[-2]

result = 0
# print(first)
while True:
    for i in range(k):
        if m == 0:
            break;
        result += first
        m -= 1
    if m == 0:
        break;
    result += second
    m -= 1
    
print(result)