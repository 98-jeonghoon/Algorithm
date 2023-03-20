from bisect import bisect_left, bisect_right

n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
target = list(map(int, input().split()))

def counting(card, value):
    left = bisect_left(card, value)
    right = bisect_right(card, value)
    return abs(left - right)

for tar in target:
    a = counting(card, tar)
    print(a, end=' ')