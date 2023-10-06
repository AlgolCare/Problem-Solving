import heapq

n = int(input())
cls = [list(map(int, input().split())) for i in range(n)]
cls.sort()

pq = []
heapq.heappush(pq, cls[0][1])

for i in range(1, n):
    if cls[i][0] >= pq[0]:
        heapq.heapreplace(pq, cls[i][1])
    else:
        heapq.heappush(pq, cls[i][1])
print(len(pq))
