def solution(m, n, board):
    maps = []
    for i in board:
        maps.append(list(i))
    answer = 0
    remove = set()
    
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                now = maps[i][j]
                if maps[i][j] == []:
                    continue
                if maps[i][j+1] == now and maps[i+1][j] == now and maps[i+1][j+1] == now:
                    remove.add((i, j))
                    remove.add((i+1, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j+1))
                    
        if remove:
            answer += len(remove)
            for a, b in remove:
                maps[a][b] = []
            remove = set()
        else:
            return answer
        
        while True:
            cnt = 0
            for i in range(m - 1):
                for j in range(n):
                    if maps[i][j] and maps[i+1][j] == []:
                        maps[i+1][j] = maps[i][j]
                        maps[i][j] = []
                        cnt = 1
            if cnt == 0:
                break


# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
