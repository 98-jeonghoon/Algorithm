def solution(board):
    w, h = len(board[0]), len(board)
    dp = [[0] * w for _ in range(h)]
    dp[0] = board[0]
    for i in range(1, h):
        dp[i][0] = board[i][0]
    
    for i in range(1, h):
        for j in range(1, w):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    print(dp)
    answer = 0
    for i in range(h):
        tmp = max(dp[i])
        answer = max(answer, tmp)
    
    return answer ** 2
# def solution(board):
#     width, height = len(board[0]), len(board)
#     board_size = min(width, height)
#     while board_size:
#         for w in range(0, width - board_size + 1):
#             for h in range(0, height - board_size + 1):
#                 if is_square(board, w, h, board_size):
#                     return board_size ** 2
#         board_size -= 1
#     return 0

# def is_square(board, w, h, board_size):
#     for i in range(h, h + board_size):
#         for j in range(w, w + board_size):
#             if board[i][j] == 0:
#                 return False
#     return True

# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
# print(solution([[1,0,1,1],[0,0,0,1],[0,1,0,1],[0,1,0,0]]))