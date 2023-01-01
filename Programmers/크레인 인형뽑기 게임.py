def check(n):
    stack = []
    
def solution(board, moves):
    answer = 0
    arr = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if not arr:
                    arr.append(board[j][i-1])
                elif arr[-1] == board[j][i-1]: 
                    arr.pop(-1)
                    answer += 1
                else:
                    arr.append(board[j][i-1])
                board[j][i-1] = 0
                break
            else:
                continue
    return answer * 2

print(solution([[0,0,0,0,0],
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]], [1,5,3,5,1,2,1,4]))