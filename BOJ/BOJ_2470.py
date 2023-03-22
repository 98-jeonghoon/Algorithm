n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = len(liquid) - 1
answer = abs(liquid[start] + liquid[end])
final = [liquid[start], liquid[end]]

while start < end:
    left_value = liquid[start]
    right_value = liquid[end]

    mix = left_value + right_value

    if abs(mix) < answer:
        answer = abs(mix)
        final = [left_value, right_value]
        if answer == 0:
            break
    
    if mix < 0:
        start += 1
    else:
        end -= 1

print(final[0], final[1])