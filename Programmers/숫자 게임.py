## 시간 초과 코드
# def solution(A, B):
#     answer = 0
#     for i in A:
#         stack = []
#         for j in B:
#             if j > i:
#                 stack.append(j)
#         if len(stack) > 0:
#             answer += 1
#             value = min(stack)
#             B.remove(value)
        
#     return answer

## 정석 풀이
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    for a in A:
        if a < B[i]:
            answer += 1
            i += 1
    return answer


## 최대힙을 이용한 풀이
import heapq

def solution(A, B):
    A = [-i for i in A]
    B = [-i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)
    answer = 0
    while A and B:
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        if -a < -b:
            answer += 1
        else:
            heapq.heappush(B, b)
    return answer   

print(solution([5,1,3,7], [2,2,6,8]))
# print(solution([2,2,2,2], [1,1,1,1]))