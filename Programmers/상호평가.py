def solution(scores):
    new_arr = [[] * len(scores) for _ in range(len(scores))]
    for i in range(len(new_arr)):
        for score in scores:
            new_arr[i].append((score[i]))
    
    for i in range(len(new_arr)):
        max_score = max(new_arr[i])
        min_score = min(new_arr[i])
        if new_arr[i][i] == max_score and new_arr[i].count(max_score) == 1:
            new_arr[i].remove(max_score)
        elif new_arr[i][i] == min_score and new_arr[i].count(min_score) == 1:
            new_arr[i].remove(min_score)

    def grade(point):
        if point >= 90:
            return 'A'
        elif 80 <= point < 90:
            return 'B'
        elif 70 <= point < 80:
            return 'C'
        elif 50 <= point < 70:
            return 'D'
        elif point < 50:
            return 'F'
    answer = ''
    for score in new_arr:
        total = sum(score)
        avg = total / len(score)
        answer += grade(avg)
    print(answer)

# solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]])
# solution([[50, 90], [50, 87]])
# solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]])

