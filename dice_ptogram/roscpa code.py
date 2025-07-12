from collections import deque
import math

# 주사위 문양 정의
SC = "sc"
RO = "ro"
PA = "pa"

# 주사위 초기 상태
def create_dice():
    return [
        [None, SC, None],
        [RO, PA, RO],
        [None, SC, None]
    ]

# 주사위 굴리기 함수
def roll(dice, direction):
    new_dice = [row[:] for row in dice]
    if direction == 'u':
        new_dice[0][1], new_dice[1][1], new_dice[2][1] = dice[1][1], dice[2][1], dice[1][0]
    elif direction == 'r':
        new_dice[1][2], new_dice[1][1], new_dice[1][0] = dice[1][1], dice[1][0], dice[1][2]
    return new_dice

# 안전한 좌표인지 확인
def safe(a, b, n, m):
    return 0 <= a <= n and 0 <= b <= m

# DFS 기반 전체 탐색: 오른쪽, 위쪽 방향으로만 이동
def dfs(x, y, dice, path, visited, goal_x, goal_y, target_face, all_paths):
    if (x, y) == (goal_x, goal_y):
        if dice[1][1] == target_face:
            all_paths.append(path[:])
        return

    directions = {'r': (1, 0), 'u': (0, 1)}
    for dir_key, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if safe(nx, ny, goal_x, goal_y):
            ndice = roll(dice, dir_key)
            state = (nx, ny, ndice[1][1], ndice[0][1], ndice[1][0])  # 위치 + 윗, 앞, 왼 면
            if state not in visited:
                visited.add(state)
                path.append(dir_key)
                dfs(nx, ny, ndice, path, visited, goal_x, goal_y, target_face, all_paths)
                path.pop()
                visited.remove(state)

#main 함수
# 입력
goal_x, goal_y = 5, 8
target_face = RO

# 처리
start_dice = create_dice()
visited = set()
all_paths = []


#print(math.comb(goal_x + goal_y, goal_x))

dfs(0, 0, start_dice, [], visited, goal_x, goal_y, target_face, all_paths)

# 출력
print(all_paths, len(all_paths))
