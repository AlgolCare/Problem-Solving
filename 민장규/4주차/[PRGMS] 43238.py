import heapq as hq

def solution(n, times):
    heap = []
    for i in times :
        hq.heappush(heap, [i, 1])
    
    answer = 0
    for _ in range(n) :
        cnt, num = hq.heappop(heap)
        answer = cnt
        hq.heappush(heap, [cnt+cnt//num, num+1])
    return answer