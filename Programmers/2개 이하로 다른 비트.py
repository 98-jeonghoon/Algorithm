## TC 10, 11 시간초과 코드

# def find(num):
#     bin_num = bin(num)[2:]
#     while True:
#         count = 0
#         num += 1
#         new_bin_num = bin(num)[2:]
#         if len(bin_num) != len(new_bin_num):
#             new_bin_num = new_bin_num.zfill(len(bin_num))
#             bin_num = bin_num.zfill(len(new_bin_num))
#         # if len(new_bin_num)
#         for i in range(len(bin_num)):
#             if bin_num[i] != new_bin_num[i]:
#                 count += 1
        
#         if count <= 2:
#             return num


# def solution(numbers):
#     answer = []
#     for i in numbers:
#         answer.append(find(i))
#     return answer

# print(solution([2, 7]))
# print(find(2))

# Solve Code
def solution(numbers):
    answer = []

    for number in numbers:
        bin_num = list('0' + bin(number)[2:])
        idx = ''.join(bin_num).rfind('0')
        bin_num[idx] = '1'

        if number % 2 == 1:
            bin_num[idx + 1] = '0'
        
        answer.append(int(''.join(bin_num), 2))
    
    return answer

print(solution([2, 7]))