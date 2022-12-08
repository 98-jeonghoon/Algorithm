import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
rg_count = 0
r_count = 0
g_count = 0
b_count = 0

greed = []
for _ in range(N):
    greed.append(list(map(str,input().rstrip())))
rg_greed = copy.deepcopy(greed)

def RedGreenEqual(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if rg_greed[x][y] == 'R' or rg_greed[x][y] == 'G':
        rg_greed[x][y] = 'Z'
        RedGreenEqual(x + 1, y)
        RedGreenEqual(x - 1, y)
        RedGreenEqual(x, y + 1)
        RedGreenEqual(x, y - 1)
        return True
    return False

def ColorArea(x,y,color):

    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if greed[x][y] == color:
        greed[x][y] = 'Z'
        ColorArea(x + 1, y, color)
        ColorArea(x - 1, y, color)
        ColorArea(x, y + 1, color)
        ColorArea(x, y - 1, color)
        return True
    return False

for i in range(N):
    for j in range(N):
        if ColorArea(i,j,'R') == True:
            r_count += 1
        if ColorArea(i,j,'G') == True:
            g_count += 1
        if ColorArea(i,j,'B') == True:
            b_count += 1

for i in range(N):
    for j in range(N):
        if RedGreenEqual(i,j) == True:
            rg_count += 1

print(r_count + g_count + b_count, rg_count + b_count)