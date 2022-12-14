def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer


print(solution(3, ["Jeju", "Pangyo", "NewYork", "newyork"]))