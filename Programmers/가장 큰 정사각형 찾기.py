dddddddddds



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
# print(solution([[0,0,1,1],[1,1,1,1]]))