from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    length = len(numbers)
    queue.append([-numbers[0], 0])
    queue.append([+numbers[0], 0])
    
    while queue :
        num, idx = queue.popleft()
        if idx+1 == length :
            if num == target:
                answer += 1
        else :
            queue.append([num - numbers[idx + 1], idx + 1])
            queue.append([num + numbers[idx + 1], idx + 1])
    
    return answer

solution([4,1,2,1], 4)