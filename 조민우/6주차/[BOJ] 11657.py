import math
INF = math.inf
N, M = map(int, input().split())
root = [list(map(int, input().split())) for _ in range(M)]
temp = [INF for _ in range(N)]
temp[0] = 0
for i in range(N-1):
    for j in range(M):
        start, end, length = root[j][0], root[j][1], root[j][2]
        temp[end-1] = min(temp[end-1], temp[start-1]+length)
for i in range(M):
    start, end, length = root[i][0], root[i][1], root[i][2]
    if temp[end-1] > temp[start-1]+length:
        print(-1)
        exit()
for i in range(1, N):
    if temp[i] == INF:
        print(-1)
    else:
        print(temp[i])