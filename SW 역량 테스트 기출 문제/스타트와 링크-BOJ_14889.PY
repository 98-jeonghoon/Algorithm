N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (N+1)
answer = 1e9

def solve(depth, idx):
    global answer
    if depth == (N // 2): # N // 2 번만큼 재귀를 돌면
        start, link = 0, 0 #start팀과 link팀 0으로 선언
        for i in range(N): 
            for j in range(i + 1, N): #이중 리스트의 열은 굳이 0부터 돌필요가 없기 때문에 i + 1 로 범위를 좁혀준다. 
                if visited[i] and visited[j]: #만약 i,j 둘다 방문 했다면 
                    start += (graph[i][j] + graph[j][i]) #방문한 사람을 스타트팀에 더해준다.
                elif not visited[i] and not visited[j]: # 방문 안한 i j 는 링크팀이므로
                    link += (graph[i][j] + graph[j][i])  #방문안한 사람을 링크팀에 더해준다
        answer = min(answer, abs(start - link)) #[최솟값을 결과값에 대입
        return
<<<<<<< HEAD:SW 역량 테스트 기출 문제/BOJ_14889.PY
    for i in range(idx, N):
        if not visited[i]: #만약 방문을 안했다면
            visited[i] = True #방문으로 처리
            solve(depth + 1, i + 1) #재귀를 돈다 
            visited[i] = False #방문 완료 처리
=======
    for i in range(idx, N): 
        if visited[i]: #만약 방문을 했다면
            continue
        visited[i] = True #방문으로 처리
        solve(depth + 1, i + 1) #재귀를 돈다 
        visited[i] = False #방문 완료 처리
>>>>>>> 015f9fdfcb8ae1f976254acc5b9e549c25a66264:SW 역량 테스트 기출 문제/스타트와 링크-BOJ_14889.PY


solve(0, 0)
print(answer)