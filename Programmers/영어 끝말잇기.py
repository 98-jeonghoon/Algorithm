def solution(n, words):
    arr = []
    number, order = 0, 0
    arr.append(words[0])
    last_word = words[0][-1]
    for i in range(1, len(words)):
        if words[i] not in arr and words[i][0] == last_word:
            arr.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i % n) + 1
            order = (i // n ) + 1
            break
        

    return [number, order]