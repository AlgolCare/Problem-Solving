import heapq
n = int(input())
time = [list(map(int, input().split())) for i in range(n)]
q = []
time.sort()
for t in time:
    if q and q[0] <= t[0]:
        heapq.heappop(q)
    heapq.heappush(q, t[1])
print(len(q))