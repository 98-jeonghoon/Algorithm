N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

total = num[0]
max_num = -1e9
min_num = 1e9

def calc(depth, total, add, sub, mul, div):
    global max_num, min_num
    if depth == N:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return
    if add:
        calc(depth+1, total + num[depth], add-1, sub, mul, div)
    if sub:
        calc(depth+1, total - num[depth], add, sub-1, mul, div)
    if mul:
        calc(depth+1, total * num[depth], add, sub, mul - 1, div)
    if div:
        calc(depth+1, int(total / num[depth]), add, sub, mul, div - 1)

calc(1, total, add, sub, mul, div)
print(max_num)
print(min_num)