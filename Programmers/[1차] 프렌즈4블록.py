def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    answer = 0
    rm = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    rm.add((i, j))
                    rm.add((i+1, j))
                    rm.add((i, j+1))
                    rm.add((i+1, j+1))
            
        if rm:
            answer += len(rm)
            for i, j in rm:
                board[i][j] = []
            rm = set()
        else:
            return answer
        
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n-1):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
