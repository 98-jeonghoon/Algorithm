# s = input()
# boom = input()

# while boom in s:
#     s = s.replace(boom, '')

# if s == '':
#     print('FRULA')
# else:
#     print(s)

s = input()
boom = input()
len_boom = len(boom)

stack = []

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-len_boom:]) == boom:
        for _ in range(len_boom):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
