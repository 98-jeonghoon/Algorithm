from itertools import *

def solution(k, dungeons):
    case = list(permutations(dungeons))
    answer = 0
    for i in range(len(case)):
        firo = k
        count = 0
        for j in range(len(case[i])):
            if case[i][j][0] <= firo:
                firo = firo - case[i][j][1]
                count += 1
            answer = max(answer, count)  
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))