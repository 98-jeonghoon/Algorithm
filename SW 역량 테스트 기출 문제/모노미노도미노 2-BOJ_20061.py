blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]

#블록을 놓기
def put_block_blue(t, x, y):
    y = 0
    if t == 1:
        while blue[x][y] == 0 and y < 5:
            y += 1
        if blue[x][y] == 1:
            y -= 1
    elif t == 2:
        while blue[x][y] == 0 and blue[x][y + 1] == 0 and  y < 4:
            y += 1
        if blue[x][y] == 1 or blue[x][y + 1] == 1:
            y -= 1
        blue[x][y + 1] = 1
    elif t == 3:
        while blue[x][y] == 0 and blue[x + 1][y] == 0 and y < 5:
            y += 1
        if blue[x][y] == 1 or blue[x + 1][y] == 1:
            y -= 1
        blue[x + 1][y] = 1
    blue[x][y] = 1
        
def put_block_green(t, x, y):
    x = 0
    if t == 1:
        while green[x][y] == 0 and x < 5:
            x += 1
        if green[x][y] == 1:
            x -= 1
    elif t == 2:
        while green[x][y] == 0 and green[x][y + 1] == 0 and x < 5:
            x += 1
        if green[x][y] == 1 or green[x][y + 1] == 1:
            x -= 1
        green[x][y + 1] = 1
    elif t == 3:
        while green[x][y] == 0 and green[x + 1][y] == 0 and x < 4:
            x += 1
        if green[x][y] == 1 or green[x + 1][y] == 1:
            x -= 1
        green[x + 1][y] = 1
    green[x][y] = 1


# check_blue 제거할수 있나 확인
def check_blue():
    global answer
    for y in range(2, 6):
        count = 0
        for x in range(4):
            if blue[x][y] == 1:
                count += 1
        if count == 4:
            # 정답을 1 올려주고, 블록 지우고 채우기
            answer += 1
            for x in range(4):
                blue[x][y] = 0
            for change_y in range(y, 0, -1):
                for x in range(4):
                    blue[x][change_y] = blue[x][change_y - 1]
                    blue[x][change_y - 1] = 0

def push_blue():
    global blue
    cur_c = -1
    for c in range(2):
        for r in range(4):
            if blue[r][c] == 1:
                cur_c = c
                break
        if cur_c != -1:
            break
    # 밝은 곳에 숫자가 없으면 return
    if cur_c == -1:
        return

    temp_blue = [[0] * 6 for _ in range(4)]
    push_num = 0
    # 두 칸 밀기
    if cur_c == 0:
        push_num = 2
    # 한 칸 밀기
    elif cur_c == 1:
        push_num = 1

    for c in range(2, 6):
        for r in range(4):
            temp_blue[r][c] = blue[r][c - push_num]

    blue = [temp[:] for temp in temp_blue]

    
                    
def check_green():
    global answer
    for x in range(2, 6):
        count = 0
        for y in range(4):
            if green[x][y] == 1:
                count += 1
        if count == 4:
            answer += 1
            for y in range(4):
                green[x][y] = 0
            for change_x in range(x, 0, -1):
                for y in range(4):
                    green[change_x][y] = green[change_x - 1][y]
                    green[change_x - 1][y] = 0
    
def push_green():
    global green
    cur_r = -1
    for r in range(2):
        for c in range(4):
            if green[r][c] == 1:
                cur_r = r
                break
        if cur_r != -1:
            break

    # 밝은 곳에 숫자가 없으면 return
    if cur_r == -1:
        return

    temp_green = [[0] * 4 for _ in range(6)]
    push_num = 0
    # 두 칸 밀기
    if cur_r == 0:
        push_num = 2
    # 한 칸 밀기
    elif cur_r == 1:
        push_num = 1

    for r in range(2, 6):
        for c in range(4):
            temp_green[r][c] = green[r - push_num][c]

    green = [temp[:] for temp in temp_green]
    
n = int(input())
answer = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    put_block_blue(t, x, y)
    put_block_green(t, x, y)
    check_blue()
    check_green()
    push_blue()
    push_green()

count = 0

for x in range(4):
    for y in range(2, 6):
        if blue[x][y] == 1:
            count += 1

for x in range(2, 6):
    for y in range(4):
        if green[x][y] == 1:
            count += 1

print(answer)
print(count)
