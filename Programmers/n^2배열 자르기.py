def solution(n, left, right):
    # answer = []
    # graph = [[0]*n for _ in range(n)]
    # arr = []
    # for i in range(n):
    #     for j in range(n):
    #         graph[i][j] = (max(i, j) + 1)
    #         answer.append(graph[i][j])

    # return answer[left:right+1]
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    return answer

print(solution(4,7,14))