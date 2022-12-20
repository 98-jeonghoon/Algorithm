from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    count = list(count.items())
    count.sort(key= lambda x:x[1], reverse=True)
    
    for i in count:
        if k <= 0:
           break
        k -= i[1]
        answer += 1
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))