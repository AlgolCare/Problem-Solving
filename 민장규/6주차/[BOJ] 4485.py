INF = 1000000

N = int(input())
cost = []
for _ in range(N) :
    cost.extend(list(map(int, input().split())))
node = [[0 for _ in range(N*N)] for _ in range(N*N)]

for end in range(N*N) :
    if end == 0 : 
        continue
    elif end % N == 0 :
        node[end-N][end] = cost[end]
        node[end][end-N] = cost[end]
    elif end < N :
        node[end-1][end] = cost[end]
        node[end][end-1] = cost[end]
    else :
        node[end-N][end] = cost[end]
        node[end][end-N] = cost[end]
        node[end-1][end] = cost[end]
        node[end][end-1] = cost[end]