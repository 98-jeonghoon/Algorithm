import sys
#큐를 사용하기 위해 임포트
from collections import deque

n = int(sys.stdin.readline())
#티셔츠 번호를 큐에 넣어줌
queue =deque([i for i in range(1,n+1) ])
#단계
t =1

#한명이 남으려면 항상 인원수-1번째까지 해야함.
for i in range(n-1):
    #몇번째 사람이 탈락하는지 구하기
    number = (t**3) % len(queue)
    # 첫번째 사람이 탈락하면 배열의 값을 바꿀 필요가 없다.
    if number == 1:
        queue.popleft()
    #첫번째 사람이 탈락하는게 아니라면
    #number-1번째 사람이 탈락한다.
    #왼쪽(시작하는 쪽)에서 number-1번째 사람이 탈락해야하므로
    #매개변수를 음수로 넣어준다.
    else:    
        queue.rotate(-(number-1))            
        queue.popleft()
    # 단계를 한 단계씩 높여준다.   
    t+=1
#남아있는 한명의 티셔츠 번호를 출력한다.
print(*queue)
