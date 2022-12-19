from itertools import product
def solution(word):
    answer = []
    words = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for j in product(words, repeat=i):
            answer.append(''.join(j))
    answer.sort()
    
    return answer.index(word) + 1


print(solution("AAAAE"))