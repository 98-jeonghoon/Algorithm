def solution(phone_book):
    ### solution 3 ---> hash로 풀이
    # hash_map = {}
    # for number in phone_book:
    #     hash_map[number] = 1
    
    # for phone_number in phone_book:
    #     jubdoo = ''
    #     for number in phone_number:
    #         jubdoo += number
    #         if jubdoo in hash_map and jubdoo != phone_number:
    #             return False

    # return True

    ## solution 2 --> 통과
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
    
    ## solution 1 -> 시간초과
    # for i in range(len(phone_book) - 1):
    #     if phone_book[i+1].startswith(phone_book[i]):
    #         return False
    # return True

print(solution(["119", "97674223", "1195524421"]))