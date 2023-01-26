def solution(gems):
    answer = []
    shortest = 1e9
    size = len(set(gems))
    left, right = 0, 0
    gem_dic = dict()

    while right < len(gems):
        if gems[right] not in gem_dic:
            gem_dic[gems[right]] = 1
        else:
            gem_dic[gems[right]] += 1
        
        right += 1
        
        if len(gem_dic) == size:
            while left < right:
                if gem_dic[gems[left]] > 1:
                    gem_dic[gems[left]] -= 1
                    left += 1
                elif shortest > right - left:
                    shortest = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))