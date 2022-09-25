# start = 첫번째 기둥
# destination = 목표 기둥
# via = 보조기둥

n = int(input())

def hanoi(n, start, destination, via):
    if n == 1:
        print(start, destination)
        return
    hanoi(n-1, start, via, destination)
    print(start, destination)
    hanoi(n-1, via, destination, start)

print(2**n - 1)
hanoi(n, 1, 3, 2)