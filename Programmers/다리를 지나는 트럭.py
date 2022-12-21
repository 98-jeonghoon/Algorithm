def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0
    if sum(truck_weights) <= weight:
        return bridge_length + len(truck_weights)
    bridge = [0 for _ in range(bridge_length)]
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
    return answer



print(solution(2, 10, [7,4,5,6]))