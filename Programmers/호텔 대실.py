# def change_time(time):
#     hour, minutes = time.split(':')
#     return 60 * int(hour) + int(minutes)

# def solution(book_time):
#     import heapq
#     room = []
#     book_time.sort(key=lambda x : x[0])
#     for i in book_time:
#         come = change_time(i[0])
#         out = change_time(i[1]) + 10
#         if len(room) != 0 and room[0] <= come:
#             heapq.heappop(room)
#         heapq.heappush(room, out)        
#     return len(room)

def time2val(time):
    return int(time[:2]) * 60 + int(time[3:5])
def solution(book_time):
    dic = {}
    for book in book_time:
        st = time2val(book[0])
        en = time2val(book[1])
        for t in range(st,en+10):
            if dic.get(t) == None:
                dic[t] = 1
            else:
                dic[t] += 1
    
    return max(dic.values())


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))