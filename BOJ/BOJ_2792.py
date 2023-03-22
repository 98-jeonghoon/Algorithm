n, m = map(int, input().split())
dia = []

for _ in range(m):
    dia.append(int(input()))

# 보석을 가장 적게 받는 학생
start = 1
# 보석을 제일 많이 받는 학생
end = max(dia)
answer = end
while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for i in dia:
        mok = i // mid
        remain = i % mid
        total += mok

        if remain > 0 :
            total += 1
    
    if total > n :
        start = mid + 1
    else:
        answer = min(answer, mid)
        end = mid - 1
        
print(answer)