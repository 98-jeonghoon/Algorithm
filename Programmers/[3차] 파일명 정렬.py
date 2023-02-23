def solution(files):
    answer = []
    head, num, tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                num = file[i:]

                for j in range(len(num)):
                    if not num[j].isdigit():
                        tail = num[j:]
                        num = num[:j]
                        break
                answer.append([head, num, tail])
                head, num, tail = '', '', ''
                break
    
    answer = sorted(answer, key= lambda x : (x[0].upper(), int(x[1])))

    return [''.join(i) for i in answer]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))