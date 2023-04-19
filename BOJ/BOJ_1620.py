n, m = map(int, input().split())

arr = [input() for _ in range(n)]
find = [input() for _ in range(m)]
dic = dict()
for idx, name in enumerate(arr, start=1):
    if name not in dic:
        dic[name] = str(idx)
    if idx not in dic:
        dic[str(idx)] = name

for i in find:
    print(dic[i])