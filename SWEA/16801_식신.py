# t = int(input())
# n, k = map(int, input().split())
# peopel = list(map(int, input().split()))
# food = list(map(int, input().split()))

# cnt = 0

# while cnt < k:
#     cnt += 1
#     idx = 0
#     max_value = -1e9
#     for i in range(n):
#         if max_value < peopel[i] * food[i]:
#             max_value = peopel[i] * food[i]
#             idx = i
#     peopel[idx] -= 1

# # print(peopel)
# # print(food)
# answer = -1e9
# for i in range(n):
#     answer = max(answer, peopel[i] * food[i])
# print(answer)

def min_time(A, F, k):
    low, high = 0, 10**12
    while low < high:
        mid = (low + high) // 2
        training_needed = 0
        for i in range(len(A)):
            training_needed += max(0, A[i] - (mid // F[i]))
        if training_needed <= k:
            high = mid
        else:
            low = mid + 1
    return low

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    A.sort()
    F.sort(reverse=True)
    print("#{} {}".format(_ + 1, min_time(A, F, k)))