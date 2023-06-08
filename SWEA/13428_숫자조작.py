def min_max_swap(num):
    num_str = str(num)
    num_list = list(num_str)
    min_value, max_value = num, num
    
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            swapped = num_list[:]
            swapped[i], swapped[j] = swapped[j], swapped[i]
            
            if swapped[0] != '0':
                new_value = int("".join(swapped))
                min_value = min(min_value, new_value)
                max_value = max(max_value, new_value)
                
    return min_value, max_value


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    min_val, max_val = min_max_swap(n)
    print("#{} {} {}".format(test, min_val, max_val))
