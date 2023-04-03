# 누적합 알고리즘

## 1차원 배열에서의 누적합
arr = [1, 2, 3, 4, 5, 6, 10]
sum_arr = [0] * (len(arr) + 1)


# 0부터 순서대로 누적합 구하기
# for i in range(1, len(sum_arr)):
#     sum_arr[i] = sum_arr[i - 1] + arr[i]

from itertools import accumulate

def add(x, y):
    return x * y

result = list(accumulate(arr[2:]))
print(result)