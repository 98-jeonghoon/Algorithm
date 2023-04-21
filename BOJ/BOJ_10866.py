from collections import deque

n = int(input())
commands = []
queue = deque()

for _ in range(n):
    s = input()
    commands.append(s)

for command in commands:
    if 'push_front' in command:
        command = command.split()
        queue.appendleft(int(command[-1]))
    elif 'push_back' in command:
        command = command.split()
        queue.append(int(command[-1]))
    elif 'pop_front' in command:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'pop_back' in command:
        if queue:
            print(queue.pop())
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
        