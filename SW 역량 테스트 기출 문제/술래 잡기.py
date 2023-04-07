n, m, h, k = map(int, input().split())
run_people = [[[] for _ in range(n)] for _ in range(n)]
next_run_people = [[[] for _ in range(n)] for _ in range(n)]
seeker_pos = (n // 2, n // 2)
for _ in range(m):
    x, y, d = map(int, input().split())
    run_people[x-1][y-1].append(d)

graph = [[0] * n for _ in range(n)]
tree = [[False] * n for _ in range(n)]

fowarding_face = True

for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True

seeker_next_dir = [[0] * n for _ in range(n)]

seeker_rev_dir = [[0] * n for _ in range(n)]

def snail():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x, y = n // 2, n // 2
    d, check = 0, 0
    dist = 1
    while True:
        check += 1
        for _ in range(dist):
            seeker_next_dir[x][y] = d
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx, ny) == (-1, 0):
                return
            if d >= 2:
                seeker_rev_dir[nx][ny] = d - 2
            else:
                seeker_rev_dir[nx][ny] = d + 2
            x, y = nx, ny

        if check == 2:
            dist += 1
            check = 0
        d = (d + 1) % 4

snail()

def move_runner(x, y, move_dir):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    nx = x + dx[move_dir]
    ny = y + dy[move_dir]

    if nx < 0 or ny < 0 or nx >= n or ny>= n:
        if move_dir < 2:
            move_dir = 1 - move_dir
        else:
            5 - move_dir
        nx = x + dx[move_dir]
        ny = y + dy[move_dir]
    
    if (nx, ny) != seeker_pos:
        next_run_people[nx][ny].append(move_dir)
    else:
        next_run_people[x][y].append(move_dir)

def dist_from_seeker(x, y):
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)

def move_all():
    for i in range(n):
        for j in range(n):
            next_run_people[i][j] = []
    
    for i in range(n):
        for j in range(n):
            if dist_from_seeker(i, j) <= 3:
                for move_dir in run_people[i][j]:
                    move_runner(i,j, move_dir)
            else:
                for move_dir in run_people[i][j]:
                    next_run_people[i][j].append(move_dir)
    
    for i in range(n):
        for j in range(n):
            run_people[i][j] = next_run_people[i][j]

def get_seeker_dir():
    x, y = seeker_pos
    move_dir = 0

    if fowarding_face:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]
    return move_dir

def check_facing():
    global fowarding_face

    if seeker_pos == (0, 0) and fowarding_face:
        fowarding_face = False
    if seeker_pos == (n // 2, n // 2) and not fowarding_face:
        fowarding_face = True

def seeker_move():
    global seeker_pos
    x, y = seeker_pos

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    move_dir = get_seeker_dir()

    seeker_pos = (x + dx[move_dir], y + dy[move_dir])

    check_facing()

answer = 0
def get_score(t):
    global answer

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x, y = seeker_pos

    move_dir = get_seeker_dir()

    for dist in range(3):
        nx = x + dx[move_dir] * dist
        ny = y + dy[move_dir] * dist

        if 0 <= nx < n and 0 <= ny < n:
            if tree[nx][ny] == False:
                answer += t * len(run_people[nx][ny])
                run_people[nx][ny] = []

def simulate(t):
    move_all()
    seeker_move()
    get_score(t)

for t in range(1, k + 1):
    simulate(t)

print(answer)