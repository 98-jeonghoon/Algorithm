n = int(input())
array = []
for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array.sort(key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')