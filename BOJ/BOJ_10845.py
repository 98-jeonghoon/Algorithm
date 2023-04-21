from collections import deque

queue = deque()
n = int(input())
commands = []

for _ in range(n):
    s = input()
    commands.append(s)

for command in commands:
    if 'push' in command:
        command = command.split()
        queue.append(command[-1])
    elif 'pop' in command:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if queue:
            print(0)
        else:
            print(1)
    elif 'front' in command:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in command:
        if queue:
            print(queue[-1])
        else:
            print(-1)
    