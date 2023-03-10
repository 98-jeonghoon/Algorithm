n = int(input())
graph = [[0] * (n + 1)]
for i in range(n):
    graph.append([0] + list(map(int, input().split())))

answer = 1e9
total = 0
for i in range(n + 1):
    total += sum(graph[i])

def calc(x, y, d1, d2):
    tmp = [[0] * (n + 1) for _ in range(n + 1)]
    tmp[x][y] = 5
    for i in range(1, d1 + 1):
        tmp[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        tmp[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        tmp[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        tmp[x + d2 + i][y + d2 -i] = 5
        
    section1, section2, section3, section4, section5 = 0, 0, 0, 0, 0
    
    # section 1
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if tmp[r][c] == 5:
                break
            else:
                section1 += graph[r][c]
    
    # section 2
    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if tmp[r][c] == 5:
                break
            else:
                section2 += graph[r][c]
    
    #section 3
    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if tmp[r][c] == 5:
                break
            else:
                section3 += graph[r][c]
                
    #section 4
    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 - 1, - 1):
            if tmp[r][c] == 5:
                break
            else:
                section4 += graph[r][c]
    
    section5 = total - (section1 + section2 + section3 + section4)
    return max(section1, section2, section3, section4, section5) - min(section1, section2, section3, section4, section5)
    

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                 if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    answer = min(answer, calc(x, y, d1, d2))

print(answer)