def solution(dirs):
    answer = 0
    visited = set()
    move_types = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x, y = 5, 5
    for dir in dirs:
        for i in range(len(move_types)):
            if dir == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx > 10 or ny > 10:
                    continue
                if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
                    visited.add((x,y,nx,ny))
                    answer += 1
                x, y = nx , ny
                 
    return answer


print(solution("ULURRDLLU"))