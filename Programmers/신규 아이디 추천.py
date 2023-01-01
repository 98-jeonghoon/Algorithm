def stage1(s):
    s = s.lower()
    return s

def stage2(s):
    import string
    arr = list(string.ascii_letters+string.digits+'-'+'_'+'.')
    for i in s:
        if i not in arr:
            s = s.replace(i, '')
    return s

def stage3(s):
    import re
    return re.sub(r'\.{2,}', '.', s)
    
def stage4(s):
    if s.startswith('.'):
        s = s[1:]
    if s.endswith('.'):
        s = s[:-1]
    return s

def stage5(s):
    if not s:
        s += 'a'
    return s

def stage6(s):
    if len(s) >= 16:
        s = s[0:15]
        if s[-1] == '.':
            s = s.rstrip('.')
    return s

def stage7(s):
    while len(s) <= 2:
        s += s[-1]
    return s
        
def solution(new_id):
    new_id = stage1(new_id)
    new_id = stage2(new_id)
    new_id = stage3(new_id)
    new_id = stage4(new_id)
    new_id = stage5(new_id)
    new_id = stage6(new_id)
    new_id = stage7(new_id)
    return new_id

print(solution(	"...!@BaT#*..y.abcdefghijklm"))

