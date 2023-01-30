# from collections import deque
# def solution(begin, target, words):
#     answer = 0
#     tmp = 1e9
#     if target not in words:
#         return 0
#     visited = [False] * (len(words))
#     for idx, word in enumerate(words):
#         if len(set(word) - set(begin)) == 1:
#             visited[idx] = True
#             answer = bfs(word, words, target, visited)
#             answer = min(answer, tmp)
#     return answer

# def bfs(start, words, target, visited):
#     count = 0
#     queue = deque()
#     queue.append()
#     while queue:
#         now = queue.popleft()
#         if now == target:
#             return count
#         for idx, word in enumerate(words):
#             if len(set(word) - set(now)) == 1 and not visited[idx]:
#                 visited[idx] = True
#                 count += 1
#                 queue.append(word)

#     return count

from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()
    queue.append([begin, 0])
    visited = [False] * len(words)
    while queue:
        word, count = queue.popleft()
        if word == target:
            return count
        for i in range(len(words)):
            tmp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
                if tmp_cnt == 1:
                    visited[i] = True
                    queue.append([words[i], count+1])

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))