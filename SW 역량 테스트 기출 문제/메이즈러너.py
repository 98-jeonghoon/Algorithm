n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
player_pos = []
exit_pos = []
for _ in range(m):
    x, y = map(int, input().split())
    player_pos.append((x - 1, y - 1))

exit_x, exit_y = map(int, input().split())
exit_pos.append((exit_x - 1, exit_y - 1))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move_player():
    pass

def rotate_90():
    pass

def find_square():
    pass

# 벽은 회전할때마다 내구도가 1씩 깎인다.
# 내구도가 0이되면 빈칸으로 변경
# 참가자가 출구에 이동하면 즉시 탈출
# 상하좌우 움직이기 가능
# 출구까지 최단 거리가 가까운 칸으로 이동
# 한칸에 2명 모험가 가능

# 미로 회전
# 한명이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾음
# 가장 작은 크기를 갖는 정사각형이 2개이상이면 r, c 가 작은것이 우선시
# 시계방향으로 90도 회전하며 회전된 벽은 내구도 1 깎인다.

# 모든 참가자가 탈출하면 게임 끝, 게임 끝났을때 이동거리 합과 출구 좌표

