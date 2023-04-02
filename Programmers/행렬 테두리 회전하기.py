def solution(rows, columns, queries):
    answer = []
    graph = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1
    for x in range(rows):
        for y in range(columns):
            graph[x][y] = num
            num += 1
    
    for x1, y1, x2, y2 in queries:
        tmp = graph[x1 -1][y1 - 1]
        min_value = tmp
        
        for x in range(x1 - 1, x2 - 1):
            change = graph[x + 1][y1 - 1]
            graph[x][y1 - 1] = change
            min_value = min(min_value, change)
        
        for y in range(y1 - 1, y2 - 1):
            change = graph[x2 - 1][y + 1]
            graph[x2 - 1][y] = change
            min_value = min(min_value, change)
        
        for x in range(x2 - 1, x1 - 1, -1):
            change = graph[x - 1][y2 - 1]
            graph[x][y2 - 1] = change
            min_value = min(min_value, change)
        
        for y in range(y2 - 1, y1 - 1, -1):
            change = graph[x1 - 1][y - 1]
            graph[x1 - 1][y] = change
            min_value = min(min_value, change)
        
        graph[x1 - 1][y1] = tmp
        answer.append(min_value)
    
            
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))