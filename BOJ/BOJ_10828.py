n = int(input())
stack = []

commands = []
for _ in range(n):
    s = input()
    commands.append(s)

for command in commands:
    if 'push' in command:
        command = command.split(' ')
        stack.append(int(command[-1]))
    elif 'pop' in command:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if stack:
            print(0)
        else:
            print(1)
    elif 'top' in command:
        if stack:
            print(stack[-1])
        else:
            print(-1)
