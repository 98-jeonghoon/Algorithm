def solution(land):
    answer = 0
    idx = 1e9
    for i in range(len(land)):
        if idx == land[i].index(max(land[i])):
            continue
        answer += max(land[i])
        idx = land[i].index(max(land[i]))
    print(answer)

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
# land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
# print(land[0].index(5))