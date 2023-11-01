import heapq
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
min, sum = 1000000001, 0
for i in range(n-1):
    if min > price[i]:
        min = price[i]
    sum += min * dist[i]
print(sum)