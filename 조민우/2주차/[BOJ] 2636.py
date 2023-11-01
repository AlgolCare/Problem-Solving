n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for i in range(n)]
melt = [list(0 for i in range(m)) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day = 0

def isFinish():
    for i in cheese:
        if i.count(1) != 0:
            return 1
    return 0

def check(a, b):
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
            if cheese[nx][ny] < 0:
                return 1
    return 0

def bfs(a, b):
    global day
    queue = [[a, b]]
    visit[a][b] = 1
    find.append([a,b])
    while(queue):
        x = queue[0][0]
        y = queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                if cheese[nx][ny] == 1 and visit[nx][ny] == 0:
                    if check(nx, ny):
                        find.append([nx,ny])
                    visit[nx][ny] = 1
                    queue.append([nx,ny])

def findAir():
    global day
    queue = [[0, 0]]
    while(queue):
        x = queue[0][0]
        y = queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                if cheese[nx][ny] <= 0 and cheese[nx][ny] != -day:
                    cheese[nx][ny] = -day
                    queue.append([nx,ny])

while(isFinish()):
    visit = [list(0 for i in range(m)) for i in range(n)]
    find = []
    day += 1
    findAir()
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1 and visit[i][j] == 0:
                bfs(i, j)
    for i in find:
        melt[i[0]][i[1]] = day
        cheese[i[0]][i[1]] = 0
print(day)
count = 0
for i in melt:
    count += i.count(day)
print(count)
