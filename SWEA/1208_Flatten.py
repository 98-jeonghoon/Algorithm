t = 11

for test in range(1, t):
    dump = int(input())
    box = list(map(int, input().split()))

    while dump > 0:
        dump -= 1
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))
        box[max_idx] -= 1
        box[min_idx] += 1

    print(f'#{test} {max(box) - min(box)}')