n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
player_pos = []

for _ in range(m):
    x, y = map(int, input().split())
    player_pos.append((x - 1, y - 1))

exit_x, exit_y = map(int, input().split())
# 탈출구를 따로 관리해주면 복잡하므로, 탈출구를 graph의 -10으로 처리
graph[exit_x - 1][exit_y - 1] = -10
exit_pos = (exit_x - 1, exit_y - 1)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move_player(player_pos):
    exit_x, exit_y = exit_pos
    for i in range(len(player_pos)):
        x, y = player_pos[i]
        # 탈출구와의 거리를 구한다.
        dis = abs(exit_x - x) + abs(exit_y - y)
        for d in range(4):
            # 상 하 좌 우 순서대로 체크한다
            nx = x + dx[d]
            ny = y + dy[d]
            # 해당 좌표로 움직일수 있는지 체크한다.
            if 0 <= nx < n and 0 <= ny < n:
                # 해당 좌표가 출구랑 더 가까운지 체크한다.
                if abs(nx - exit_x) + abs(ny - exit_y) < dis:
                    # 만약 탈출구라면 해당 좌표를 바꿔준다.
                    if graph[nx][ny] == -10:
                        player_pos[i] = (-10, -10)
                        break
                    # 만약 0이라면 이동가능한 지점이다
                    # 해당 좌표를 움직여준다.
                    elif graph[nx][ny] == 0:
                        player_pos[i] = (nx, ny)
                        break


# 탈출구에 위치한 플레이어를 제거해준다.
def remove_exit_player(player_pos):
    for _ in range(len(player_pos)):
        x, y = player_pos.pop(0)
        # 만약 해당 좌표가 탈출구라면 그냥 제거
        if (x, y) == (-10, -10):
            continue
        # 탈출구가 아니라면 다시 player_pos에 진입
        else:
            player_pos.append((x, y))

move_player(player_pos)
remove_exit_player(player_pos)
print(player_pos)

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

