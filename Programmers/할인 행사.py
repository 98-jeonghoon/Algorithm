def solution(want, number, discount):
    answer = 0
    dic = dict()
    for i in range(len(number)):
        dic[want[i]] = number[i]

    from collections import Counter

    for i in range(len(discount) - 9):
        counter = Counter(discount[i:i+10])
        if counter == dic:
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
