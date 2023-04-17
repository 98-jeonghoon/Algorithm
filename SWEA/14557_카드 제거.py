T = int(input())
for test_case in range(1, T + 1):
    h = input()
    if h.count('0') == len(h):
         print('#%d %s' %(test_case, 'no'))
         continue
    if h.count('1')%2 == 1:
         print('#%d %s' %(test_case, 'yes'))
         continue
    if h.count('1')%2 == 0:
         print('#%d %s' %(test_case, 'no'))
         continue