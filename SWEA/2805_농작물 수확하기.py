def get_diamond_values(arr):
    diamond_values = []
    center_row = len(arr) // 2
    center_col = len(arr[0]) // 2

    # 상단 절반
    for row in range(center_row + 1):
        for col in range(center_col - row, center_col + row + 1):
            diamond_values.append(arr[row][col])

    # 하단 절반
    for row in range(center_row + 1, len(arr)):
        for col in range(center_col - (len(arr) - row - 1), center_col + (len(arr) - row)):
            diamond_values.append(arr[row][col])

    return diamond_values

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    diamond = get_diamond_values(graph)
    diamond = [int(i) for i in diamond]
    print('#{} {}'.format(test, sum(diamond)))

