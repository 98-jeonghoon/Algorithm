# 체스판 0, 0 이 black인 경우, white 인 경우 2가지를 구해야됨

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
arr = []
for x in range(n - 7):
    for y in range(m - 7):
        count1 = 0
        count2 = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if graph[i][j] != 'W':
                        count1 += 1
                    if graph[i][j] != 'B':
                        count2 += 1
                else:
                    if graph[i][j] != 'B':
                        count1 += 1
                    if graph[i][j] != 'W':
                        count2 += 1
        arr.append(min(count1, count2))

print(min(arr))