n, r, c = map(int, input().split())
answer = 0
def recursion(x, y, n):
    global answer
    # if x < 0 or y < 0 or x >= n or y >= n:
    #     return
    if x == r and y == c:
        print(answer)
        exit(0)
    if n == 1:
        answer += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        answer += n * n
        return
    
    length = n // 2
    recursion(x, y, length)
    recursion(x, y + length, length)
    recursion(x + length, y, length)
    recursion(x + length, y + length, length)

recursion(0, 0, 2 ** n)

print(answer)