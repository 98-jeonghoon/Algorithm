from collections import Counter

n = int(input())

arr = []

for _ in range(n):
    num = int(input())
    arr.append(num)

arr.sort()
counter = Counter(arr)
print(round(sum(arr) / len(arr)))
print(arr[len(arr) // 2])
counter = counter.most_common(2)
if len(counter) > 1 :
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(counter[0][0])
print(max(arr) - min(arr))
# print(int(sum(arr)/len(arr)))