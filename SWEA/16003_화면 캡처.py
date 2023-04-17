# t = int(input())
# for test in range(t):
#     n = int(input())
#     arr = [i for i in range(1, n + 1)]

#     arr.sort(key=lambda x:ascii(x))
#     arr = arr[:50]

#     arr = [str(i) + '.png' for i in arr]
#     print('#{}'.format(test + 1), end=' ')
#     print(*arr)

from queue import PriorityQueue

def generate_filenames(n):
    q = PriorityQueue()
    for i in range(1, 10):
        q.put((str(i), i))
        
    filenames = []
    while len(filenames) < min(50, n):
        curr_str, curr_num = q.get()
        filenames.append(curr_str + '.png')
        
        for i in range(10):
            next_str = curr_str + str(i)
            next_num = int(next_str)
            if next_num <= n:
                q.put((next_str, next_num))
            else:
                break
                
    return filenames

t = int(input().strip())
for test in range(t):
    n = int(input().strip())
    arr = generate_filenames(n)
    print('#{}'.format(test + 1), end=' ')
    print(*arr)

