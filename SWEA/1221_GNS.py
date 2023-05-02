t = int(input())
dic_word = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
dic_num = {0 : "ZRO", 1 : "ONE", 2 : "TWO", 3 : "THR", 4 : "FOR", 5 : "FIV", 6 : "SIX", 7 : "SVN", 8 : "EGT", 9 : "NIN"
}
for test in range(1, t + 1):
    s, n = input().split()
    word = list(input().split())
    arr = []
    for i in word:
        arr.append(dic_word[i])
    arr.sort()
    print(s)
    for i in arr:
        print(dic_num[i], end=' ')

