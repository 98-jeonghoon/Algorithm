n = int(input())
word = []
for _ in range(n):
    w = input()
    word.append(w)

word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
    print(i)
