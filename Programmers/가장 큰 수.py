def solution(numbers):
    num_list = list(map(str, numbers))
    num_list.sort(key = lambda x:x*3, reverse=True)
    return str(int(''.join(num_list)))