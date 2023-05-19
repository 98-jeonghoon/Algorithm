# def solution(x, y, n):
#     answer = 0
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
    
#     return dp[y]

# print(solution(10, 40, 5))

# def solution(numbers, k):
#     answer = ''
#     stack = []

#     for number in numbers:
#         while stack and k > 0 and stack[-1] < number:
#             stack.pop()
#             k -= 1
#         stack.append(number)
#     if k != 0:
#         stack = stack[:-k]
#     for i in stack:
#         answer += i
#     print(answer)
#     return answer

# solution('1924', 2)

# solution('1231234', 3)

# def solution(numbers):
#     from itertools import permutations
#     answer = 0
#     arr = []
#     for i in range(1, len(numbers) + 1):
#         for j in list(permutations(numbers, i)):
#            arr.append(''.join(j))

#     def prime(x):
#         import math
#         for i in range(2, int(math.sqrt(x)) + 1):
#             if x % i == 0:
#                 return False
#         return True
#     arr = list(set(list(map(int, arr))))
#     print(arr)
#     for i in arr:
#         if int(i) == 0 or int(i) == 1:
#             continue
#         if prime(int(i)):
#             answer += 1
#     print(answer)
#     return answer
    
# solution('011')

# def solution(numbers):
#     num_list = list(map(str, numbers))
#     num_list.sort(key=lambda x : x * 3, reverse=True)
#     return str(int(''.join(num_list)))
# print(solution([0, 0, 0, 0]))
# solution([3, 30, 34, 5, 9])

# def solution(topping):
#     from collections import Counter
#     counter = Counter(topping)
#     answer =0
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

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0 for _ in range(bridge_length)]

#     while bridge:
#         answer += 1
#         bridge.pop(0)
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 t = truck_weights.pop(0)
#                 bridge.append(t)
#             else:
#                 bridge.append(0)
#     return answer

# print(solution(2, 10, [7,4,5,6]))

# def solution(numbers):
#     stack = []
#     answer = [-1 for _ in range(len(numbers))]
#     stack.append(0)

#     for i in range(1, len(numbers)):
#         while stack and numbers[stack[-1]] < numbers[i]:
#             answer[stack.pop()] = numbers[i]
#         stack.append(i)

# solution([2,3,3,5])

# def solution(numbers):
#     arr = []
#     for number in numbers:
#         bin_number = bin(number)[2:]
#         bin_len = len(bin_number)
#         while True:
#             count = 0
#             number += 1
#             bin_number_2 = bin(number)[2:]
#             bin_number_2 = bin_number_2[-bin_len:]
#             for i in range(len(bin_number)):
#                 if bin_number[i] != bin_number_2[i]:
#                     count += 1
#             if count <= 2:
#                 arr.append(number)
#                 break
#     print(arr)

# solution([2, 7])

# def solution(word):
#     from itertools import product
#     arr = ['A','E','I','O','U']
#     answer = []
#     for i in range(1, len(arr) + 1):
#         for case in list(product(arr, repeat=i)):
#             answer.append(''.join(case))
#     answer.sort()
#     return answer.index(word) - 1

# print(solution('AAAE'))


# def solution(skill, skill_trees):
#     answer = 0
#     for skills in skill_trees:
#         stack = ''
#         for i in skills:
#             if i in skill:
#                 stack += i
#         print(stack)
#         if skill[:len(stack)] == stack:
#             answer += 1
#         print(answer)
#     return answer

# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# def solution(prices):
#     from collections import deque
#     queue = deque(prices)
#     answer = []
#     while queue:
#         count = 0
#         now = queue.popleft()

#         for i in queue:
#             count += 1
#             if now > i:
#                 break
#         answer.append(count)
#     return answer

# print(solution([1,2,3,2,3]))

# def solution(clothes):
#     dic = dict()
#     answer = 0
#     for value, key in clothes:
#         if key not in dic:
#             dic[key] = [value]
#         else:
#             dic[key].append(value)
#     arr = list(dic.values())
#     for i in arr:
#         answer *= len(i) + 1
#     return answer - 1
# solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

# def solution(prices):
#     from collections import deque
#     answer = []
#     queue = deque(prices)
#     while queue:
#         count = 0
#         now = queue.popleft()
#         for i in queue:
#             count += 1
#             if now > i:
#                 break
#         answer.append(count)
#     print(answer)
#     return answer

# solution([1,2,3,2,3])
# solution([3,2,4,2,6,7])

# def solution(scoville, k):
#     answer = 0
#     import heapq
#     heapq.heapify(scoville)
#     while True:
#         if len(scoville) == 1 and scoville[0] < k:
#             return -1
#         first = heapq.heappop(scoville)
#         if first < k:
#             answer += 1
#             second = heapq.heappop(scoville)
#             mix = first + second * 2
#             heapq.heappush(scoville, mix)
#         else:
#             return answer
# solution([1,2,3,9,10,12], 7)

# def convert(num, base):
#     import string
#     q, r = divmod(num, base)
#     number = string.digits + string.ascii_uppercase
#     if q == 0:
#         return number[r]
#     else:
#         return convert(q, base) + number[r]

# def solution(want, number, discount):
#     answer = 0
#     from collections import Counter
#     dic = dict()
#     for want, num in zip(want, number):
#         dic[want] = num
#     for i in range(len(discount) - 9):
#         counter = Counter(discount[i:i+10])
#         if counter == dic:
#             answer += 1
#     print(answer)
#     return answer

# def solution(numbers, target):
#     answer = 0
#     def back_tracking(depth, cnt):
#         nonlocal answer
#         if depth == len(numbers):
#             if cnt == target:
#                 answer += 1
#                 return
#         else:
#             back_tracking(depth + 1, cnt + numbers[depth])
#             back_tracking(depth + 1, cnt - numbers[depth])
#     back_tracking(0, 0)
#     return answer


# print(solution([1, 1, 1, 1, 1], 3))

# def isPalindrome(x):
#     if x==x[::-1]:
#         return True
# def solution(s):
#     MAX=0
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             if isPalindrome(s[i:j]):
#                 if MAX<len(s[i:j]):
#                     MAX=len(s[i:j])
#     return MAX

# solution('abcdcba')

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]


# for i in range(1, len(graph)):
#     graph[i][0] = min(graph[i - 1][1], graph[i - 1][2]) + graph[i][0]
#     graph[i][1] = min(graph[i - 1][0], graph[i - 1][2]) + graph[i][1]
#     graph[i][2] = min(graph[i - 1][0], graph[i - 1][1]) + graph[i][2]

# print(min(graph[n-1]))

# s = input()

# arr = []
# for i in s:
#     if i in ['(', ')' ,'[', ']']:
#         arr.append(i)

# stack = []


# for i in arr:
#     if stack == []:
#         stack.append(i)
#     else:
#         if stack[-1] == '(' and i == ')':
#             stack.pop()
#         elif stack[-1] == '[' and i == ']':
#             stack.pop()
#         else:
#             stack.append(i)

# if stack == []:
#     print(1)
# else:
#     print(0)

# dijkstra

# n = int(input())
# m = int(input())

# graph = [[] * (n + 1) for _ in range(n + 1)]
# distance = [1e9] * (n + 1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# start, destination = map(int, input().split())

# def dijkstra(start):
#     import heapq
#     queue = []
#     # heapq에 cost, 방문노드 순으로 넣음
#     heapq.heappush(queue, (0, start))
#     distance[start] = 0

#     while queue:
#         dist, now = heapq.heappop(queue)
#         # 현재 비용이 더 작을경우 바꿔줄 필요가 없음
#         if distance[now] < dist:
#             continue
    
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(queue, (cost, i[0]))

# dijkstra(start)
# print(distance[destination])


n, m, x = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    import heapq
    INF = int(1e9)
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if dist < distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance


answer = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    answer = max(answer, go[x] + back[i])
print(answer)