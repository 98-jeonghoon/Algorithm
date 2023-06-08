# def solution(k, tangerine):
#     from collections import Counter
#     answer = 0
#     counter = Counter(tangerine)
#     counter = list(counter.items())
#     counter.sort(key=lambda x : x[1], reverse=True)
#     for i in counter:
#         if k <= 0:
#             break
#         k -= i[1]
#         answer += 1
#     return answer
        

# print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
# print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))

# def solution(elements):
#     answer = 0
#     elements_len = len(elements)
#     elements = elements * 2
#     arr = []
#     # print(elements_len)
#     for i in range(1, elements_len+1):
#         for j in range(0, elements_len):
#             arr.append(sum(elements[j:j+i]))
#     arr = list(set(arr))
#     return len(arr)

# print(solution([7,9,1,1,4]))

# def solution(people, limit):
#     answer = 0
#     start = 0
#     end = len(people) - 1
#     people.sort()
#     while start <= end:
#         if people[start] + people[end] <= limit:
#             answer += 1
#             start, end = start + 1, end - 1
#         else:
#             end -= 1
#             answer += 1
#     return answer

# print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))

# def solution(n, words):
#     number, order = 0, 0
#     check = []
#     last_word = words[0][-1]
#     check.append(words[0])
#     for i in range(1, len(words)):
#         if words[i] not in check and words[i][0] == last_word:
#             check.append(words[i])
#             last_word = words[i][-1]
#         else:
#             number = (i % n) + 1
#             order = (i // n) + 1
#             break
#     return [number, order]
            
        

# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

# def solution(s):
#     answer = []
#     s = s[2:-2]
#     s = s.split('},{')
#     s.sort(key=len)
#     for i in s:
#         i = i.split(',')
#         for j in i:
#             if int(j) not in answer:
#                 answer.append(int(j))
#     # print(answer)
#     return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{20,111},{111}}"))

# def solution(progresses, speeds):
#     from collections import deque
#     arr = []
#     for i in range(len(progresses)):
#         cnt = 0
#         while True:
#             if progresses[i] >= 100:
#                 arr.append(cnt)
#                 break
#             cnt += 1
#             progresses[i] += speeds[i]
#     queue = deque(arr)
#     answer = []
#     while queue:
#         res = 1
#         now = queue.popleft()
#         while queue and now >= queue[0]:
#             queue.popleft()
#             res += 1
#         answer.append(res)
#     return answer
         
# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))

from collections import deque
# def solution(priorites, location):
#     queue = deque()
#     for idx, prior in enumerate(priorites):
#         queue.append((idx, prior))
#     # print(max_queue)
#     answer = 0
#     while queue:
#         max_prior = max(queue, key = lambda x : x[1])[1]
#         idx, prior = queue.popleft()
#         if queue and prior < max_prior:
#             queue.append((idx, prior))
#         else:
#             answer += 1
#             if idx == location:
#                 break
# #     return answer
# print(solution([2,1,3,2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))

# def solution(str1, str2):
#     str1, str2 = str1.upper(), str2.upper() 
#     str1_arr, str2_arr = [], []
    
#     for i in range(len(str1) - 1):
#         s = str(str1[i] + str1[i + 1])
#         if s.isalpha():
#             str1_arr.append(s)

#     for i in range(len(str2) - 1):
#         s = str(str2[i] + str2[i + 1])
#         if s.isalpha():
#             str2_arr.append(s)

#     from collections import Counter
#     counter1 = Counter(str1_arr)
#     counter2 = Counter(str2_arr)
#     inter = sum((counter1 & counter2).values())
#     union = sum((counter1 | counter2).values())
    
#     if inter == 0 and union == 0:
#         return 65536
#     else:
#         return int(inter / union * 65536)

# print(solution('FRANCE', 'french'))
# print(solution('handshake', 'shake hands'))

from collections import Counter
# def solution(want, number, discount):
#     answer = 0
#     dic = dict()
#     for w, n in zip(want, number):
#         dic[w] = n
#     for i in range(len(discount) - 9):
#         c = Counter(discount[i:i+10])
#         if dic == c:
#             answer += 1
#     return answer


# print(solution(["banana", "apple", "rice", "pork", "pot"], [3,2,2,2,1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))

# def solution(phone_book):
#     from collections import defaultdict
#     dic = defaultdict(int)
#     for i in phone_book:
#         dic[i] = 1
#     dic = dic.keys()
    
#     for phone in phone_book:
#         s = ''
#         for i in phone:
#             s += i
#             if s in dic and s != phone:
#                 return False
#     return True
    
    

# print(solution(["119", "97674223", "1195524421"]))

# def convert(num, base):
#     import string
#     tmp = string.digits + string.ascii_lowercase
#     q, r = divmod(num, base)
#     if q == 0:
#         return tmp[r]
#     else:
#         return convert(q, base) + tmp[r]

# def is_prime(x):
#     import math
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

# def solution(n, k):
#     answer = 0
#     n = convert(n, k)
#     tmp = n.split('0')
#     for i in tmp:
#         if i == '1' or i == '':
#             continue
#         else:
#             if is_prime(int(i)):
#                 answer += 1
#     return answer

# print(solution(437674, 3))
# print(solution(110011, 10))

# def solution(msg):
#     result = []
#     dic = dict()
#     for i in range(1, 27):
#         dic[chr(64 + i)] = i
    

#     i = 0
#     check = ''
#     result = []
#     num = 27
    
#     while i < len(msg):
#         check += msg[i]
#         if check in dic:
#             i+=1
#         else:
#             dic[check] = num
#             num += 1
#             result.append(dic[check[:-1]])
#             check = ''
#     result.append(dic[check])
#     return result


# print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))

# def convert(num, base):
#     import string
#     tmp = string.digits + string.ascii_uppercase

#     q, r = divmod(num, base)
#     if q == 0:
#         return tmp[r]
#     else:
#         return convert(q, base) + tmp[r]

# def solution(n, t, m, p):
#     answer = ''
#     tmp = ''
#     for i in range(0, t*m):
#         tmp += (convert(i, n))
#     # print(tmp)
#     for i in range(p - 1, m * t, m):
#         answer += tmp[i]
#     # print(answer)
#     return answer
# print(solution(2, 4, 2, 1))
# print(solution(16, 16, 2, 1))

# def solution(scoville, K):
#     import heapq
#     heapq.heapify(scoville)
#     cnt = 0
#     if scoville[0] >= K:
#         return cnt
    
#     while scoville[0] < K and len(scoville) > 1:    
#         mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
#         heapq.heappush(scoville, mix)
#         cnt += 1
#     if scoville[0] >= K:
#         return cnt
#     else:
#         return -1

# print(solution([1,2,3,9,10,12], 7))


# def solution(prices):
#     from collections import deque
#     queue = deque(prices)
#     answer = []
#     while queue:
#         cnt = 0
#         now = queue.popleft()

#         for i in range(len(queue)):
#             cnt += 1
#             if now > queue[i]:
#                 break
#         answer.append(cnt)

#     return answer

# print(solution([1, 2, 3, 2, 3]))

# def solution(records):
#     dic = dict()
#     answer = []
#     for record in records:
#         record = record.split()
#         if record[0] == 'Enter' or record[0] == 'Change':
#             dic[record[1]] = record[2]
    
#     for record in records:
#         record = record.split()
#         if record[0] == 'Enter':
#             answer.append((f'{dic[record[1]]}님이 들어왔습니다.'))
#         elif record[0] == 'Leave':
#             answer.append((f'{dic[record[1]]}님이 나갔습니다.'))
#     return answer

# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# def change_minutes(time) -> int:
#     time = time.split(':')
#     return int(time[0]) * 60 + int(time[1])
# def solution(fees, records):
#     basic_time, basic_fee, unit_time, unit_fee = fees
#     dic = dict()

#     for record in records:
#         time, num, state = record.split()
#         time = change_minutes(time)
#         if num not in dic:
#             dic[num] = [(time, state)]
#         else:
#             dic[num].append((time, state))
    
#     dic = list(dic.items())
#     dic.sort(key= lambda x : x[0])
    
#     for dics in dic:
        

# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

# def solution(maps):
#     from collections import deque
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     def bfs(x, y):
#         visited = [[False] * len(maps[0]) for _ in range(len(maps))]
#         visited[x][y] = True
#         queue = deque()
#         queue.append((x, y))
#         while queue:
#             x, y = queue.popleft()
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#                 if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
#                     if visited[nx][ny] == False and maps[nx][ny] == 1:
#                         maps[nx][ny] = maps[x][y] + 1
#                         visited[nx][ny] = True
#                         queue.append((nx, ny))
#         # for i in maps:
#         #     print(i)
#         return maps[len(maps) - 1][len(maps[0]) - 1]
#     answer = bfs(0, 0)
#     if answer > 1:
#         return answer
#     else:
#         return -1
                        
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

# def solution(dirs):
#     answer = 0
#     # UDRL
#     n = 10
#     graph = [[0] * n for _ in range(n)]
#     move_type = ['U', 'D', 'L', 'R']
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, 1, -1]
#     x, y = n // 2, n // 2
#     check = []

#     for dir in dirs:
#         for i in range(len(move_type)):
#             if move_type[i] == dir:
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or ny < 0 or nx > n or ny > n:
#                     continue
#                 if (x, y, nx, ny) not in check and (nx, ny, x, y) not in check:
#                     check.append((x, y, nx, ny))
#                     answer += 1
#                 x, y = nx, ny
    
#     return answer

# print(solution('ULURRDLLU'))
# print(solution('LULLLLLLU'))

# def solution(skill, skill_trees):
#     answer = 0
#     skill_arr = list(skill)
#     tmp = []
#     for skill_tree in skill_trees:
#         s = ''
#         for i in skill_tree:
#             if i in skill_arr:
#                 s += i
#         tmp.append(s)
#     for i in tmp:
#         if i == skill[:len(i)]:
#             answer += 1
    
#     return answer

# print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))

# def solution(files):
#     pass

# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

# def solution(number, k):
#     stack = []
#     answer = ''
    
#     for i in number:
#         while stack and k > 0 and i > stack[-1]:
#             stack.pop()
#             k -= 1
#         stack.append(i)
#     if k:
#         stack = stack[:-k]
#     for i in stack:
#         answer += i
#     return answer
# print(solution('1924', 2))

# def solution(n):
#     # 움직임은 (하, 우, 상좌)
#     dx = [1, 0, -1]
#     dy = [0, 1, -1]
#     graph = [[0] * n for _ in range(n)]
#     direct = 0
#     total = 0
#     for i in range(1, n + 1):
#         total += i

#     num = 1
#     x, y = 0, 0

#     while num <= total:
#         graph[x][y] = num
#         num += 1
#         nx = x + dx[direct]
#         ny = y + dy[direct]

#         if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             direct = (direct + 1) % 3
#             nx = x + dx[direct]
#             ny = y + dy[direct]
#             x, y = nx, ny
    
#     answer = []
#     for x in range(n):
#         for y in range(n):
#             if graph[x][y] != 0:
#                 answer.append(graph[x][y])
#     return answer


# def solution(topping):
#     answer = 0
#     counter = Counter(topping)
#     check = set()
#     for i in topping:
#         counter[i] -= 1
#         check.add(i)
#         if counter[i] == 0:
#             counter.pop(i)
#         if len(counter) == len(check):
#             answer += 1
        
#     return answer
    
# print(solution([1, 2, 1, 3, 1, 4, 1, 2]))

# from itertools import product, permutations

# def is_prime(x):
#     import math
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

# def solution(numbers):
#     answer = 0
#     tmp = []
#     numbers = list(numbers)
#     for i in range(1, len(numbers) + 1):
#         for j in list(permutations(numbers, i)):
#             tmp.append(''.join(j))

#     tmp = list(set(list(map(int, tmp))))
#     for i in tmp:
#         if is_prime(i) and i >= 2:
#             answer += 1
#     return answer
# print(solution('011'))

# def solution(x, y, n):
#     INF = int(1e9)
#     dp = [INF] * (y + 1)
#     dp[x] = 0
#     for i in range(x, y + 1):
#         if i + n <= y:
#             dp[i + n] = min(dp[i + n], dp[i] + 1)
#         if i * 2 <= y:
#             dp[i * 2] = min(dp[i * 2], dp[i] + 1)
#         if i * 3 <= y:
#             dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    
#     if dp[y] == INF:
#         return -1
#     else:
#         return dp[y]
    

# print(solution(10, 40, 5))

# def solution(numbers):
#     answer = [-1] * len(numbers)
#     stack = []
#     stack.append(0)
#     for i in range(1, len(numbers)):
#         while stack and numbers[stack[-1]] < numbers[i]:
#             answer[stack.pop()] = numbers[i]
#         stack.append(i)
    
#     return answer

# print(solution([2, 3, 3, 5]))

# def solution(bridge_length, weight, truck_weights):
#     bridge = [0] * bridge_length
#     time = 0
#     while bridge:
#         time += 1
#         bridge.pop(0)
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 t = truck_weights.pop(0)
#                 bridge.append(t)
#             else:
#                 bridge.append(0)
    
#     return time

# print(solution(2, 10, [7, 4, 5, 6]))

# def solution(queue1, queue2):
#     from collections import deque
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     sum_1 = sum(queue1)
#     sum_2 = sum(queue2)
#     limit = len(queue1) * 3
#     cnt = 0
#     if (sum_1 + sum_2) % 2 == 1:
#         return -1

#     while True:
#         if cnt == limit:
#             return -1
#         if sum_1 > sum_2:
#             now = queue1.popleft()
#             sum_1 -= now
#             sum_2 += now
#             queue2.append(now)
#             cnt += 1
#         elif sum_1 < sum_2:
#             now = queue2.popleft()
#             sum_1 += now
#             sum_2 -= now
#             queue1.append(now)
#             cnt += 1
#         else:
#             return cnt
        

# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))

# def solution(maps):
#     from collections import deque
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[False] * m for _ in range(n)]
#     answer = []
#     def bfs(x, y):
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#         res = 0
#         queue = deque()
#         queue.append((x, y))
#         visited[x][y] = True
#         res += int(maps[x][y])
#         while queue:
#             x, y = queue.popleft()
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#                 if 0 <= nx < n and 0 <= ny < m:
#                     if visited[nx][ny] == False and maps[nx][ny] != 'X':
#                         res += int(maps[nx][ny])
#                         visited[nx][ny] = True
#                         queue.append((nx, ny))
#         return res
    
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] != 'X' and visited[i][j] == False:
#                 answer.append(bfs(i, j))
#     answer.sort()
#     if answer == []:
#         return [-1]
#     return answer

# print(solution(["X591X","X1X5X","X231X", "1XXX1"]	))

# def solution(n, wires):
#     answer = 1e9
#     graph = [[] for _ in range(n + 1)]
#     for i, j in wires:
#         graph[i].append(j)
#         graph[j].append(i)
    
#     def bfs(graph, start, visited):
#         queue = deque([start])
#         visited[start] = True
#         count = 1

#         while queue:
#             now = queue.popleft()
#             for i in graph[now]:
#                 if not visited[i]:
#                     queue.append(i)
#                     visited[i] = True
#                     count += 1
#         return count

#     for start, not_visit in wires:
#         visited = [False] * (n + 1)
#         visited[not_visit] = True
#         count = bfs(graph, start, visited)
#         answer = min(answer, abs(count - (n - count)))


#     return answer


# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

# def change_minute(time):
#     time = time.split(':')
#     return int(time[0]) * 60 + int(time[1])
# def solution(book_time):
#     from collections import defaultdict
#     dic = defaultdict(int)
#     for start, end in book_time:
#         start, end = change_minute(start), change_minute(end)
#         for i in range(start, end + 1):
#             dic[i] += 1
    
#     return max(dic.values())


# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))

# def solution(storey):
#     answer = 0
#     while storey > 0:
#         storey, move = divmod(storey, 10)
#         if move > 5 or (move == 5 and storey % 10 >= 5):
#             move = 10 - move
#             storey += 1
#         answer += move
#     return answer

# print(solution(2554))

def solution(s):
    
