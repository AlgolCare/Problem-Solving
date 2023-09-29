import sys
import heapq
input = sys.stdin.readline

N = int(input())
room = []
for _ in range(N) :
    room.append(list(map(int, input().split())))
room = sorted(room, key=lambda x : (x[0], x[1]))

hq = [room.pop(0)[1]]
for i in room :
    if i[0] < hq[0] :
        heapq.heappush(hq, i[1])
    else : 
        heapq.heappop(hq)
        heapq.heappush(hq, i[1])

print(len(hq))