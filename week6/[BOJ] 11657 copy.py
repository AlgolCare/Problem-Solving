import sys

N, M = map(int, sys.stdin.readline().split())

road = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    road.append((A - 1, B - 1, C))

res = [int(1e9) for _ in range(N)]
temp = [0 for _ in range(N)]
res[0] = 0
cycle = False

for i in range(N):
    for j in range(M):
        c, n, d = road[j]
        if res[c] != int(1e9) and res[n] > res[c] + d:
            res[n] = res[c] + d
            if i == N - 1:
                cycle = True

if cycle:
    print(-1)
else:
    for i in range(1, N):
        print(res[i] if res[i] != int(1e9) else -1)