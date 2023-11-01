n = int(input())
roads =list(map(int, input().split()))
costs = list(map(int, input().split()))

total = roads[0] * costs[0]
check = costs[0]

for i in range(1, n - 1):
    if check > costs[i]:
        check = costs[i]
    total += check * roads[i]

print(total)

# pop 등 써서 느린 코드
# n = int(input())
# roads =list(map(int, input().split()))
# costs = list(map(int, input().split()))

# min_cost = costs.pop(0)
# total = 0
# for road in roads:
#     total += min_cost * road
#     min_cost = min(min_cost, costs.pop(0))

# print(total)



# 현재까지 방문한 가장 싼 기름값을 저장
# 시작할 떄는 당장 다음 마을까지 가는 것만 결제하기
# 그 이후에는 가장 적은 기름 * 거리만큼 계속 늘리기