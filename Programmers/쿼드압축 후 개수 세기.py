import sys
sys.setrecursionlimit(10001)
def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    def quad_tree(x, y, length):
        init = arr[x][y]

        for i in range(x, x+length):
            for j in range(y, y+length):
                if arr[i][j] != init:
                    length = length // 2
                    quad_tree(x, y, length)
                    quad_tree(x, y + length, length)
                    quad_tree(x + length, y, length)
                    quad_tree(x + length, y + length, length)
                    return
        answer[init] += 1
    quad_tree(0, 0, length)
    
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))

# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

# # 4등분 하기
# mid = len(arr) // 2

# arr_1 = [i[:mid] for i in arr[:mid]]
# arr_2 = [i[:mid] for i in arr[mid:]]
# arr_3 = [i[mid:] for i in arr[:mid]]
# arr_4 = [i[mid:] for i in arr[mid:]]

# print(arr_1)
# print(arr_2)
# print(arr_3)
# print(arr_4)