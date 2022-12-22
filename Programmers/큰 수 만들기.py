def solution(number, k):
    answer = []
    for num in number:
        while answer and k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer[:len(number)-k])
# def solution(number, k):
#     from itertools import combinations
#     number = list(number)
#     num = len(number) - k
#     arr = []
#     for i in list(combinations(number, num)):
#         arr.append(''.join(i))
#     arr.sort()
#     return arr[-1]
print(solution("4177252841", 4))
print(solution("3813132874", 6))
print(solution("956870", 3))