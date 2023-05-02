t = int(input())
for test in range(1, t + 1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()

    bread = 0
    flag = True

    for arrival_time in people:
        time_elapsed = arrival_time // m
        bread = time_elapsed * k

        # 현재 도착한 손님 전까지 붕어빵을 사용한 양 계산
        consumed_bread = 0
        for prev_time in people[:people.index(arrival_time)]:
            consumed_bread += 1

        # 현재 도착한 손님까지 모두 붕어빵을 받을 수 있는지 확인
        if bread - consumed_bread >= 1:
            continue
        else:
            flag = False
            break

    if flag:
        print(f'#{test} Possible')
    else:
        print(f'#{test} Impossible')
