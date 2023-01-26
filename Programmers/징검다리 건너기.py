# def solution(stones, k):
#     answer = 0
#     while True:
#         answer += 1
#         for i in range(len(stones)):
#             if stones[i] == 0:
#                 continue
#             else:
#                 stones[i] -= 1
#         count = 0
#         for stone in stones:
#             if stone == 0:
#                 count += 1
#                 if count == k:
#                     return answer
#             else:
#                 count = 0

def solution(stones, k):
    start = 1
    end = max(stones)
    # mid = (start + end) // 2

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
                if cnt >= k :
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
    return start

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

