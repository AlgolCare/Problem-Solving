INF = 0x7FFFFFFF
N, M = map(int, input().split())
graph = [[] for _ in range(501)]
res = [INF] * 501

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

res[1] = 0  # 처음 시작할 정점

check = False

# 각 노드마다 모든 엣지에 대해 Relax
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(len(graph[j])):
            nextV, nextCost = graph[j][k]
            if res[j] != INF and res[nextV] > res[j] + nextCost:
                res[nextV] = res[j] + nextCost
                if i == N:  # N-1까지 돌고 N번째에서 값이 갱신되면 음수 싸이클
                    check = True
                    break

if check:
    print("-1")
else:
    for i in range(2, N + 1):
        if res[i] == INF:
            print("-1")
        else:
            print(res[i])
