def solution(elements):
    answer = []
    elements_len = len(elements)
    elements = elements * 2
    for i in range(1, elements_len+1):
        for j in range(0, elements_len):
            answer.append(sum(elements[j:j+i]))

    answer = list(set(answer))
    
    return len(answer)

#     return answer
# def solution(elements):
#     answer = []
#     elements = elements * 2
#     for i in range(0, len(elements)):
#         for j in range(0, len(elements)):
#             answer.append(sum(elements[j:j+i+1]))
#     print(answer)
    
#     answer = list(set(answer))

#     return answer

print(solution([7,9,1,1,4]))

# arr = [7,9,1,1,4]

# for i in range(0, len(arr)):
#     print(arr[i:i+1], end=' ')

# print()
# for i in range(0, len(arr), 2):
#     print(arr[i:i+2], end=' ')

# print()    
# for i in range(0, len(arr), 3):
#     print(arr[i:i+3], end=' ')

# print()
# for i in range(0, len(arr), 4):
#     print(arr[i:i+4], end=" ")
