def check(user, ban):
    if len(user) != len(ban):
        return False
    else:
        for i, j in zip(user, ban):
            if j == '*':
                continue
            if i != j:
                return False
        return True
def solution(user_id, banned_id):
    from itertools import permutations
    answer = []
    arr = list(permutations(user_id, len(banned_id)))
    for i in arr:
        count = 0
        for a, b in zip(i, banned_id):
            if check(a, b):
                count += 1
            if count == len(banned_id):
                if set(i) not in answer:
                    answer.append(set(i))
    
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))