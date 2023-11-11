import heapq
import math
INF = math.inf
def dijkstra(n, arr):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit = [[INF for _ in range(n)] for _ in range(n)]
    q = [(arr[0][0], 0, 0)]
    visit[0][0] = arr[0][0]
    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if (visit[nx][ny] > dist + arr[nx][ny]):
                visit[nx][ny] = dist + arr[nx][ny]
                heapq.heappush(q, (visit[nx][ny], nx, ny))
    return visit[n-1][n-1]
cnt = 1
while True:
    n = int(input())
    if (n == 0):
        exit()
    arr = [list(map(int, input().split())) for _ in range(n)]
    print("Problem %d: %d" %(cnt,dijkstra(n, arr)))
    cnt += 1
    