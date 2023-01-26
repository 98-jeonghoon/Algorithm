def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x : x[1])
    # print(routes)
    camera = routes[0][1]
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            camera = routes[i][1]
            answer += 1
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))