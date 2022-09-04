# N = int(input())

# for i in range(1,10):
#     print(N, "*", i, "=", N*i)

# sum = 0
# T = int(input())
# for i in range(T):
#     a, b = map(int,input().split())
#     sum = a+b
#     print(a+b)

# sum = 0
# n = int(input())
# for i in range(1, n+1):
#     sum += i
# print(sum)

# import sys

# T = int(sys.stdin.readline())
# for i in range(1,T+1):
#     a, b = map(int, input().split())
#     sum = a + b
#     print("Case #{}: {} + {} = {}".format(i,a,b,sum))
    
    
# n = int(input())

# for i in range(1,n+1):
#     print(" " * (n-i) + "*"*i)

# N, X = map(int, input().split())
# P = list(map(int, input().split()))
# for i in P:
#     if i < X:
#         print(i, end=" ")

# while True:
#     try:
#         a, b = map(int,input().split())
#         print(a+b)
#     except:
#         break

# n = int(input()) #26
# num = n
# count = 0

# while True:
#     a = num%10 #2
#     b = num%10 #6
#     c = (a+b)%10 #8
#     num = (b*10)+c #68
    
#     count+=1
#     if(num==n):
#         break

# print(count)

# import sys
# a ,b = map(int,sys.stdin.readline().split())
# time = int(input())

# total_time = a *60 + b + time
# H = total_time // 60
# M = total_time % 60
# if H > 23:
#     H -= 24
# print(H, M)


# N = int(input())

# for i in range(N):
#     total = 0
#     score = 0
#     for j in input():
#         if j == "O":
#             score += 1
#             total += score
#         else:
#             score = 0
#     print(total)

# C = int(input())
# for i in range(C):
#     N = list(map(int,input().split()))
#     avg = sum(N[1:]) / N[0]
#     count = 0
#     for j in N[1:]:
#         if j > avg:
#             count += 1
#     percent = count / N[0] * 100
#     avg = 0
#     print("%.3f%%"%percent)


# a = int(input())
# b = int(input())
# c = int(input())

# total = a*b*c
# total_list = list(map(int,str(total)))

# for i in range(10):
#     print(total_list.count(i))


# n = int(input())

# for i in range(n):
#     total = 0
#     count = 0
#     for j in input():
#         if j == "O":
#             count += 1
#             total += count
#         else:
#             count = 0
#     print(total)

# def solve(a):
#     total = 0
#     for x in a:
#         total += x
#     return total


# def hansu(num):
#     count = 0
#     for i in range(1, num+1):
#         num_list = list(map(int,str(i)))
#         if i < 100:
#             count += 1
#         elif num_list[0]-num_list[1] == num_list[1] - num_list[2]:
#             count += 1
#     return count

# num = int(input())
# print(hansu(num))

# n = int(input())
# s = int(input())
# num = list(map(int,str(s)))
# print(num)

# count = 0
# for i in num:
#     count += i
    
# print(count)

# a = int(input())
# n = list(input())
# sum = 0
# for i in n:
#     sum += int(i)
# print(sum)

# a = []
# word = input()
# list = 'abcdefghijklmnopqrstuvwxyz'
# for i in list:
#     if i in word:
#         print(word.index(i), end=' ')
#     else:
#         print(-1, end=' ')

# T = int(input())
# for i in range(T):
#     R, S = list(map(str,input().split()))
#     R = int(R)
#     for j in S:
#         print(R*j, end='')
#     print()

# 문제에서 대소문자를 구분하지 않음
# words = input().lower()
# # 중복 제거해서 리스트에 넣음
# li = list(set(words))
# # 카운트용 리스트 정의
# cnt_li = []

# # i = [M, i, s, s, i, s, s, i, p, i]
# for i in li:
#     # i 리스트 원소가 words에 몇 개 있는지 카운트
#     cnt = words.count(i)
#     cnt_li.append(cnt)

# #  가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력
# if cnt_li.count(max(cnt_li)) >= 2:
#     print("?")

# else:
#     # li 리스트 중 cnt_li에서 가장 큰 수의 인덱스를 반환해서
#     # li 인덱스 원소의 문자열을 대문자로 출력
#     print(li[cnt_li.index(max(cnt_li))].upper())
    
# a,b = map(int, input().split())
# reverse_a = int(str(a)[::-1])
# reverse_b = int(str(b)[::-1])

# if reverse_a > reverse_b:
#     print(reverse_a)
# else:
#     print(reverse_b)
# # elif reverse_a < reverse_b:
#     # print(reverse_b)
# num = input()
# time = 0
# for i in num:
#     if i in ['A', 'B', 'C']:
#         time += 3
#     elif i in ['D', 'E', 'F']:
#         time += 4
#     elif i in ['G', 'H', 'I']:
#         time += 5
#     elif i in ['J', 'K', 'L']:
#         time += 6
#     elif i in ['M', 'N', 'O']:
#         time += 7
#     elif i in ['P', 'Q', 'R', 'S']:
#         time += 8
#     elif i in ['T', 'U', 'V']:
#         time += 9
#     elif i in ['W', 'X', 'Y', 'Z']:
#         time += 10
# print(time)

# N = int(input())
# count = N

# for i in range(N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             count -=1
#             break

# print(count)


# data = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# s = input()
# count = 0
# for i in data:
#     s = s.replace(i, 'a')
# print(len(s))


# word = input().lower()
# li = list(set(word))
# cnt_li = []

# for i in li:
#     cnt = word.count(i)
#     cnt_li.append(cnt)

# if cnt_li.count(max(cnt_li)) >= 2:
#     print("?")
# else:
#     print(li[cnt_li.index(max(cnt_li))].upper())


# N = int(input())
# count = N

# for i in range(N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             count -=1
#             break

# print(count)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n = int(input())
# print(fibonacci(n))
    
    
# a = int(input())
# result = 1
# for i in range(1, a+1, 1):
#     result *= i

# n = int(input())

# def recur(i, n):
#     print("____"*i + '"재귀함수가 뭔가요?"')
#     if i == n:
#         print("____"*i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
#     else:
#         print("____"*i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print("____"*i + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#         print("____"*i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         recur(i+1, n)
#     print("____"*i + "라고 답변하였지.")


# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# recur(0, n)

# def recru(num):



# N , M = map(int,input().split())
# num = list(map(int,input().split()))
# result = 0
# for i in range(0, N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             if num[i] + num[j] + num[k] > M:
#                 continue
#             else:
#                 result = max(result, num[i]+num[j]+num[k]) 
                
# print(result)    

# N = int(input())
# result = 0

# for i in range(1, N+1):        
#     a = list(map(int, str(i)))  
#     s = i + sum(a)              
#     if(s == N):                 
#         result = i                   
#         break

# print(result)

# N = int(input())
# data = []
# for _ in range(N):
#     weight, heigth = list(map(int,input().split()))
#     data.append((weight, heigth))

# for i in data:
#     rank = 1
#     for j in data:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, end=' ')


# n = int(input())
# nth = 666
# count = 0

# while True:
#     if '666' in str(nth):
#         count +=1
#     if count == n:
#         print(nth)
#         break
#     nth+=1

# import sys

# n, m = map(int, input().split())
# board = []

# for i in range(n):
#     board.append(sys.stdin.readline().rstrip()) 

# min_diff = 64

# for i in range(n-7):
#     for j in range(m-7):
#         white_first=0
#         black_first=0
#         for a in range(i, i+8):
#             for b in range(j, j+8):
#                 if (a+b)%2 == 0:
#                     if board[a][b] != 'B':
#                         black_first += 1
#                     if board[a][b] != 'W':
#                         white_first += 1 
#                 else:
#                     if board[a][b] != 'B':
#                         white_first += 1
#                     if board[a][b] != 'W':
#                          black_first += 1
#         min_diff = min(min_diff, white_first, black_first)

# print(min_diff)


# x, y = 1, 1
# dx = [0,0,-1,1] #L,R,U,D
# dy = [-1,1,0,0]
# move_type = ['L','R','U','D']
# N = int(input())
# move = list(map(str, input().split()))

# for i in move:
#     for j in range(len(move_type)):
#         if i == move_type[j]:
#             nx = x + dx[j]
#             ny = y + dy[j]
        
#     if nx < 1 or ny < 1 or nx> N or ny>N:
#         continue
        
#     x ,y = nx, ny

# print(x,y)
    
# data = input()
# for x in data:
#     if x.isalpha():
#         print(x)

# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.pop()
#         print(v, end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
                
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * 9
# bfs(graph, 1, visited)



# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
        
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * 9

# bfs(graph, 1, visited)

# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
                
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited =[False]*9
# bfs(graph, 1, visited)


# from collections import deque


# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
        
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * 9
# bfs(graph, 1, visited)

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# def dfs(x, y):
#     if x<=-1 or x >=n or y<=-1 or y>= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1

# print(result)

# from collections import deque

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]    
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny <0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph[n -1][m -1]

# print(bfs(0, 0))


# n, m = map(int,input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
    
# def dfs(x,y):
#     if x<=-1 or y<=-1 or x>=n or y>=m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# result = 0 
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1

# print(result)

from collections import deque

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y =queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or ny <0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))    