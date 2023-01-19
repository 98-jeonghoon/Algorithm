def solution(geners, plays):
    from collections import defaultdict
    answer = []
    dic = defaultdict(int)
    for key, value in zip(geners, plays):
        dic[key] += value

    dic = list(dic.items())
    dic.sort(key=lambda x:x[1], reverse=True)
    arr = []
    for idx, album in enumerate(zip(geners, plays)):
        name, play = album[0], album[1]
        arr.append((idx, name, play))
    arr.sort(key= lambda x : (x[1], -x[2], [0]))
    # print(dic)
    for i in dic:
        count = 0
        for j in arr:
            if i[0] == j[1]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(j[0])
    return answer

    # a = list(dic.items())
    # print(a[0][1])
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

# genres : ["classic", "pop", "classic", "classic", "pop"]
# plays : [800, 600, 150, 800, 2500]
# answer : [4, 1, 0, 3]