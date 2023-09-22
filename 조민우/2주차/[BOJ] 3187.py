import sys
sys.setrecursionlimit(10**6) #재귀 최대 깊이 수정

n, m = map(int, input().split())
field = [list(input()) for i in range(n)]
visit = [list(0 for i in range(m)) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    queue = [[a, b]]
    visit[a][b] = 1
    sheep, wolf = 0, 0
    if field[a][b] == 'v':
        wolf += 1
    elif field[a][b] == 'k':
        sheep += 1              #처음 인덱스 확인
    while(queue):
        x, y = queue[0][0], queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                if field[nx][ny] != '#' and visit[nx][ny] == 0:
                    if field[nx][ny] == 'v':
                        wolf += 1
                    elif field[nx][ny] == 'k':
                        sheep += 1
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
    if wolf >= sheep:
        return 0, wolf
    else:
        return sheep, 0

def dfs(a, b):
    visit[a][b] = 1
    global s, w
    if field[a][b] == 'v':
        w += 1
    elif field[a][b] == 'k':
        s += 1              #처음 인덱스 확인
    for i in range(4):
        nx, ny = a + dx[i], b + dy[i]
        if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
            if field[nx][ny] != '#' and visit[nx][ny] == 0:
                dfs(nx, ny)

wolf, sheep = 0, 0
for i in range(n):
    for j in range(m):
        if (visit[i][j] == 0 and field[i][j] != '#'):
            s, w = 0, 0
            # s, w = bfs(i, j)
            # wolf += w
            # sheep += s
            dfs(i, j)
            if w >= s:
                wolf += w
            else:
                sheep += s
print(sheep, wolf)