## 현재 기어 상태를 보고 먼저 계산한 후, 주어진 기어 회전시킴
## 처음 기어 상태 계산 한 후 (3, -1)을 회전
## (3, -1)기어 회전한걸 바탕으로 다시 현 기어상태 체크
## 마지막으로 (1, 1) 기어 회전
## 마지막 회전한후에는 맞물린거 있는지 확인 안해두됨
## 그냥 점수 계산만 해줌ㄴ

from collections import deque

graph = [deque(list(map(int, input()))) for _ in range(4)]
t = int(input())

def check_right(start, dir):
    if start > 3 or graph[start - 1][2] == graph[start][6]:
        return
    
    if graph[start - 1][2] != graph[start][6]:
        check_right(start + 1, -dir)
        graph[start].rotate(dir)
        
def check_left(start, dir):
    if start < 0 or graph[start][2] == graph[start + 1][6]:
        return
    
    if graph[start + 1][6] != graph[start][2]:
        check_left(start - 1, -dir)
        graph[start].rotate(dir)


for _ in range(t):
    num, dir = map(int, input().split())
    num -= 1
    check_right(num + 1, -dir)
    check_left(num - 1, -dir)
    graph[num].rotate(dir)
    
answer = 0
for i in range(4):
    answer += (2**i) * graph[i][0]
    
print(answer)