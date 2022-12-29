def solution(orders, course):
    from itertools import combinations
    from collections import Counter
    answer = []
    for i in course:
        arr = []
        for j in orders:
            arr += list(combinations(sorted(j), i))
        counter = Counter(arr)
        if len(counter) == 0:
            continue
        if max(counter.values()) == 1:
            continue
        for f in counter:
            if counter[f] == max(counter.values()):
                answer.append(''.join(f))
    return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

# arr = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# arr1 = []
# for i in arr:
#     for j in range(len(i)):
#         if i[j] not in arr1:
#             arr1.append(i[j])

# from itertools import combinations
# from collections import Counter
# arr2 = []
# course = [2,3,4]
# for i in course:
#     for j in arr:
#         arr2 += list(combinations(sorted(j), i))
# # print(arr2)
# counter = Counter(arr2)
# # print(counter.items())
# for f in counter:
#     if counter[f] == max(counter.values()):
#         print('a')
# # print(counter)