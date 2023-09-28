import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global sheep, wolf

    if x < 0 or x > R-1 or y < 0 or y > C-1 or graph[x][y] == '#' or graph[x][y] == '-':
        return False

    if graph[x][y] != '#':
        if graph[x][y] == 'v':
            wolf += 1
        if graph[x][y] == 'k':
            sheep += 1
        
        # 방문처리
        graph[x][y] = '-'

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

sheep_cnt, wolf_cnt = 0, 0
for i in range(R):
    for j in range(C):
        sheep, wolf = 0, 0
        if dfs(i, j):
            if sheep > wolf:
                sheep_cnt += sheep
            else:
                wolf_cnt += wolf

print(sheep_cnt, wolf_cnt)