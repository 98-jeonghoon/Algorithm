l, c = map(int, input().split())
alpah = list(map(str, input().split()))
alpah.sort()
visited = [False] * (c+1)
need_alpha = ['a', 'e', 'i', 'o', 'u']
arr = []

def backtracking(depth, idx):
    if depth == l:
        vo, co = 0, 0
        for i in range(l):
            if arr[i] in need_alpha:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(arr))
        return
    
    for i in range(idx, c):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(alpah[i])
        backtracking(depth+1, i + 1)
        visited[i] = False
        arr.pop()
        
backtracking(0, 0)
    
    
    