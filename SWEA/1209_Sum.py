for test in range(1, 11):
    t = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    
    r_sum = [sum(row) for row in graph]  # 각 행의 합 계산
    c_sum = [sum(col) for col in zip(*graph)]  # 각 열의 합 계산
    
    diag1_sum = sum(graph[i][i] for i in range(100))  # 왼쪽 대각선의 합 계산
    diag2_sum = sum(graph[i][99-i] for i in range(100))  # 오른쪽 대각선의 합 계산
    
    max_sum = max(max(r_sum), max(c_sum), diag1_sum, diag2_sum)  # 최댓값 계산
    
    print('#{} {}'.format(t, max_sum))
