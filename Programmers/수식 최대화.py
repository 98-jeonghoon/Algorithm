def parse_string(s):
    result = []
    current_number = ""
    for c in s:
        if c.isdigit():
            current_number += c
        else:
            result.append(int(current_number))
            result.append(c)
            current_number = ""
    if current_number:
        result.append(int(current_number))
    return result

def calc(expression, operator):
    arr = parse_string(expression)
    for i in operator:
        stack = []
        while len(arr) != 0:
            tmp = arr.pop(0)
            if tmp == i:
                if i == '*':
                    stack.append(str(int(stack.pop()) * int(arr.pop(0))))
                if i == '+':
                    stack.append(str(int(stack.pop()) + int(arr.pop(0))))
                if i == '-':
                    stack.append(str(int(stack.pop()) - int(arr.pop(0))))
            else:
                stack.append(tmp)
        arr = stack
    return abs(int(arr[-1]))

def solution(expression):
    from itertools import permutations
    expression_operator = []
    result = []
    operator = ['+', '-', '*']
    for i in expression:
        if i in operator:
            expression_operator.append(i)
    
    operator_list = list(permutations(list(set(expression_operator)), len(list(set(expression_operator)))))
    for i in operator_list:
        result.append(calc(expression, i))
    
    return max(result)

print(solution("100-200*300-500+20"))













# def parse_string(s):
#     result = []
#     current_number = ""
#     for c in s:
#         if c.isdigit():
#             current_number += c
#         else:
#             result.append(int(current_number))
#             result.append(c)
#             current_number = ""
#     if current_number:
#         result.append(int(current_number))
#     return result


# def operation(front, back, operator):
#     if operator == '*':
#         return str(int(front) * int(back))
#     if operator == '+':
#         return str(int(front) + int(back))
#     if operator == '-':
#         return str(int(front) - int(back))


# def calc(expression, operator):
#     arr = parse_string(expression)
#     for i in operator:
#         stack = []
#         while len(arr) != 0:
#             tmp = arr.pop(0)
#             if tmp == i:
#                 stack.append(operation(stack.pop(), arr.pop(0), i))
#             else:
#                 stack.append(tmp)
#         arr = stack
#     return abs(int(arr[-1]))

# def solution(expression):
#     from itertools import permutations
#     expression_operator = []
#     result = []
#     operator = ['+', '-', '*']
#     for i in expression:
#         if i in operator:
#             expression_operator.append(i)
    
#     operator_list = list(permutations(list(set(expression_operator)), len(list(set(expression_operator)))))
#     for i in operator_list:
#         result.append(calc(expression, i))
    
#     return max(result)

# print(solution("100-200*300-500+20"))
