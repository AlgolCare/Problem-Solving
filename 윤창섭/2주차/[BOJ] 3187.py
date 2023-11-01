import sys
from collections import deque

sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
board = [list(input()) for i in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


q = deque()

visited = [[False] * c for i in range(r)]
sheep = 0
sheeps = 0
wolf = 0
wolves = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == "v":
            wolves += 1
        elif board[i][j] == "k":
            sheeps += 1


def dfs(sy, sx):
    global wolf, sheep
    visited[sy][sx] = True
    if board[sy][sx] == "v":
        wolf += 1
    elif board[sy][sx] == "k":
        sheep += 1

    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]

        if (
            ny < 0
            or nx < 0
            or ny >= r
            or nx >= c
            or visited[ny][nx]
            or board[ny][nx] == "#"
        ):
            continue
        dfs(ny, nx)


def bfs(sy, sx):
    global wolf, sheep
    q.append([sy, sx])
    visited[sy][sx] = True
    while q:
        y, x = q.popleft()
        if board[y][x] == "v":
            wolf += 1
        elif board[y][x] == "k":
            sheep += 1

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (
                ny < 0
                or nx < 0
                or ny >= r
                or nx >= c
                or visited[ny][nx]
                or board[ny][nx] == "#"
            ):
                continue
            visited[ny][nx] = True
            q.append([ny, nx])


for i in range(r):
    for j in range(c):
        if board[i][j] != "#" and not visited[i][j]:
            wolf = 0
            sheep = 0
            bfs(i, j)
            if sheep > wolf:
                wolves -= wolf
            else:
                sheeps -= sheep


print(sheeps, wolves)

"""
양 > 늑대 일 경우 양은 늑대를 잡아먹고, 살아남는다.
양 <= 늑대일 경우 양을 모두 잡아먹힌다.

모든 양과 늑대의 수를 순회를 통해 탐색한다.

벽이 아니고, 방문한 곳이 아닌 점에 대해서 탐색을 시작한다.

dfs의 경우 재귀를 사용하여 울타리에 갇힌 양과 늑대의 수를 구한다.
이후 조건에 맞게 양과 늑대의 수를 빼준다.

bfs의 경우 queue를 사용하여 울타리에 갇힌 양과 늑대의 수를 구한다.
이때, python에서는 queue 대신 list를 사용하는데 이는 시간초과를 발생시킨다.
따라서 deque를 사용하여 queue를 구현한다.
deque의 popleft() 함수를 사용하여 일반 queue와 같은 기능을 수행하도록 한다.
이후 로직은 dfs를 사용할 경우와 동일하다

dfs를 사용한 경우 시간은 176ms이고, bfs를 사용한 경우 시간은 136ms이다.
bfs가 시간적인 면에서 더 유리하다고 할 수 있다.
"""
