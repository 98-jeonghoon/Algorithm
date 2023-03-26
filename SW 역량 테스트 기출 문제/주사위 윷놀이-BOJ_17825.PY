dice = list(map(int, input().split()))

route = [
    # 가장 바깥번째 길
    [i * 2 for i in range(21)],
    # 첫번째 파랑색을 타고 가는 길
    [10, 13, 16, 19, 25, 30, 35, 40],
    # 20의 파랑색을 타고 가는 길
    [20, 22, 24, 25, 30, 35, 40],
    # 30의 파랑색을 타고 가는 길
    [30, 28, 27, 26, 25, 30, 35, 40]
]

max_value = -1e9
horse = [[0, 0] for _ in range(4)]
# horse 의미 -> 첫번째는 해당 route에 대한 index, 두번째는 어떤 말인지

def play(n, score, horse):
    global max_value
    if n >= 10:
        max_value = max(max_value, score)
        return
    
    for h in range(4):
        if horse[h][0] != -1:
            tmp = horse[:]
            tmp[h][0] += dice[n]

            if tmp[h][1] == 0:
                if tmp[h][0] == 5:
                    tmp[h][1] = 1
                    tmp[h][0] = 0
                elif tmp[h][0] == 10:
                    tmp[h][1] = 2
                    tmp[h][0] = 0
                elif tmp[h][0] == 15:
                    tmp[h][1] = 3
                    tmp[h][0] = 0
            
            if tmp[h][0] >= len(route(tmp[h][1])):
                tmp[h][0] = -1
                play(n + 1, score, tmp)

