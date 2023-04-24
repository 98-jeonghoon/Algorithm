# t = int(input())

# for test in range(1, t + 1):
#     num = int(input())
#     idx = 1
#     while True:
#         if idx > num:
#             idx = -1
#             break
#         if num == idx ** 3:
#             break
#         idx += 1
#     print(f'{test} {idx}')

t = int(input())

def binary_search(num):
    left, right = 1, num

    while left <= right:
        mid = (left + right) // 2
        mid_cubed = mid ** 3

        if mid_cubed == num:
            return mid
        elif mid_cubed < num:
            left = mid + 1
        else:
            right = mid - 1

    return -1

for test in range(1, t + 1):
    num = int(input())
    result = binary_search(num)
    print(f'#{test} {result}')
