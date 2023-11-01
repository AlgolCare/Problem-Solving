n = int(input())
edge = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = edge[0] * cost[0] # 첫 도시에서는 무조건 주유해야함
min_cost = cost[0] # 현재까지의 최소 비용

for i in range(1, n - 1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    res += min_cost * edge[i]
print(res)
