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

def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    return music

def solution(m, musicinfos):
    import math
    answer = None
    arr = []
    m = change(m)
    for i in musicinfos:
        arr = i.split(',')
        melody = arr[-1]
        start_time = int(arr[0][:2]) * 60 + int(arr[0][3:5])
        end_time = int(arr[1][:2]) * 60 + int(arr[1][3:5])
        play_time = abs(end_time - start_time)
        melody = change(melody)
        melody = melody * math.ceil(play_time / len(melody))
        melody = melody[:play_time]
        
        if m not in melody:
            continue
        
        if answer == None or answer[0] < play_time or (answer[0] == play_time and answer[1] > start_time):
            answer = (play_time, start_time, arr[2])
    
    if answer:
        return answer[-1]
    else:
        return "(None)"
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABC", ["12:00,12:06,HELLO,ABC#ABC#ABC"]))
