from collections import deque
# for dfs
import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])

    wolf, sheep = 0, 0
    while queue:
        a, b = queue.popleft()
        if a < 0 or a >= R or b < 0 or b >= C or visited[a][b] == 1 or graph[a][b] == '#':
            continue
        else:
            if graph[a][b] == 'v':
                wolf += 1
            if graph[a][b] == 'k':
                sheep += 1
            visited[a][b] = 1
            for i, j in zip(dx, dy):
                queue.append((a + i, b + j))

    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf


def dfs(x, y):
    global g_sheep, g_wolf
    if x < 0 or x >= R or y < 0 or y >= C or visited[x][y] == 1 or graph[x][y] == '#':
        return 0
    if graph[x][y] == 'v':
        g_wolf += 1
    if graph[x][y] == 'k':
        g_sheep += 1
    visited[x][y] = 1
    for i, j in zip(dx, dy):
        dfs(x + i, y + j)


R, C = map(int, input().split())
graph = [input() for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
t_sheep, t_wolf = 0, 0

for i in range(R):
    for j in range(C):
        # bfs
        if graph[i][j] != '#' and visited[i][j] == 0: # 벽이 아닌데 방문한 적 없으면
            s, w = bfs(i, j) # 해당 구역에서 살아남은 양, 늑대 수 반환_bfs
            visited[i][j] = 1
            t_sheep += s
            t_wolf += w

        # dfs
        # g_sheep, g_wolf = 0, 0
        # if graph[i][j] != '#' and visited[i][j] == 0: # 벽이 아닌데 방문한 적 없으면
        #     dfs(i, j)
        #     if g_sheep > g_wolf:
        #         t_sheep += g_sheep
        #     else:
        #         t_wolf += g_wolf

print(t_sheep, t_wolf)

