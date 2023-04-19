# # 무지성 구현 // 시간초과
# # t = int(input())
# # for _ in range(t):
# #     k = int(input())
# #     arr = []
# #     for _ in range(k):
# #         s = input().split()
# #         if s[0] == 'I':
# #             arr.append(int(s[1]))
# #         elif s[0] == 'D':
# #             if len(arr) == 0:
# #                 continue
# #             elif s[1] == '-1':
# #                 arr.pop(arr.index(min(arr)))
# #             elif s[1] == '1':
# #                 arr.pop(arr.index(max(arr)))

# #     if arr == []:
# #         print('EMPTY')
# #     else:
# #         print(max(arr), min(arr))

# # 이중우선순위 큐로 구현
# import heapq
# t = int(input())
# for _ in range(t):
#     max_heap = []
#     min_heap = []

#     k = int(input())
#     for _ in range(k):
#         command, num = input().split()
#         num = int(num)
#         if command == 'I':
#             heapq.heappush(max_heap, -num)
#             heapq.heappush(min_heap, num)
#         else:
#             if len(min_heap) == 0:
#                 pass
#             elif num == 1:
#                 max_value = abs(heapq.heappop(max_heap))
#                 min_heap.remove(max_value)
#             elif num == -1:
#                 min_value = heapq.heappop(min_heap)
#                 max_heap.remove((-min_value))
#     if min_heap:
#         print(abs(heapq.heappop(max_heap)), heapq.heappop(min_heap))
#     else:
#         print('EMPTY')
# import sys
# import heapq

# input = sys.stdin.readline

# def clean_heap(heap, removed):
#     while heap and heap[0] in removed:
#         removed[heap[0]] -= 1
#         if removed[heap[0]] == 0:
#             del removed[heap[0]]
#         heapq.heappop(heap)

# t = int(input())
# for _ in range(t):
#     max_heap = []
#     min_heap = []
#     removed_max = {}
#     removed_min = {}

#     k = int(input())
#     for _ in range(k):
#         command, num = input().split()
#         num = int(num)
#         if command == 'I':
#             heapq.heappush(max_heap, -num)
    #         heapq.heappush(min_heap, num)
    #     else:
    #         if num == 1:
    #             if max_heap:
    #                 val = -heapq.heappop(max_heap)
    #                 removed_max[val] = removed_max.get(val, 0) + 1
    #                 clean_heap(min_heap, removed_max)
    #         elif num == -1:
    #             if min_heap:
    #                 val = heapq.heappop(min_heap)
    #                 removed_min[val] = removed_min.get(val, 0) + 1
    #                 clean_heap(max_heap, removed_min)

    # clean_heap(max_heap, removed_min)
    # clean_heap(min_heap, removed_max)
    
    # if max_heap and min_heap:
    #     max_val = -heapq.heappop(max_heap)
    #     min_val = heapq.heappop(min_heap)
    #     if max_val != min_val:
    #         print(max_val, min_val)
    #     else:
    #         print(max_val, max_val)
    # else:
    #     print('EMPTY')


import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 1_000_001

    order_num = int(input())

    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif order[0] == 'D':
            if order[1] == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap:
                    visit[min_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

# 모든 연산이 끝난후에도 ㅅ쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다. 
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')