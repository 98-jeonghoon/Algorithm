t = int(input())
for test in range(t):
    n = int(input())

    arr = []
    for i in range(0, n + 1):
        arr.append(i)

    arr1 = []
    for j in arr:
        arr1.append(-j)

    arr = arr1 + arr
    arr = list(set(arr))
    from itertools import product
    count = 0
    for x, y in product(arr, repeat=2):
        if x**2 + y**2 <= n**2:
            count += 1

    print('#{} {}'.format(test+1, count))