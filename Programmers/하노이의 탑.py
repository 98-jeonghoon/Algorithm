# start = 첫번째 기둥
# destination = 목표 기둥
# via = 보조기둥

def solution(n):
    answer = []
        
    def hanoi(n, start, destination, via):
        if n == 1:
            answer.append(list(map(int, (start, destination))))
            return
        hanoi(n-1, start, via, destination)
        answer.append(list(map(int, (start, destination))))
        hanoi(n-1, via, destination, start)
    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))