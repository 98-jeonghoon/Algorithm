def play_time(musicinfos):
    arr = []
    play_time_arr = []
    for i in musicinfos:
        play_time = ''
        for j in range(len(i)):
            if i[j].isdigit():
                play_time += i[j]
        arr.append(play_time)
    for i in arr:
        play_time_arr.append(abs((int(i[:2]) * 60 + int(i[2:4])) - (int(i[4:6]) * 60 + int(i[6:8]))))
    return play_time_arr

def solution(m, musicinfos):
    answer = ''
    arr = []
    for i in musicinfos:
        # new_musicinfos = 0
        arr = i.split(',')
        play_time = abs((int(arr[0][:2]) * 60 + int(arr[0][3:5])) - (int(arr[1][:2]) * 60 + int(arr[1][3:5])))
        if m in arr[-1]:
            return arr[2]
        if len(arr[-1]) < play_time:
            new_musicinfos = arr[-1] * (play_time // len(arr[-1]))
            if m in new_musicinfos:
                answer += arr[2]
            else:
                answer += ''
    if answer:
        return answer
    else:
        return "(None)"
        # if 
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:06,HELLO,ABC#ABC#ABC"]))
# a` = 'abcd'
# b = 'zxabcdxz'
# print(a * 2)`