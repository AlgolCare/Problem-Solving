import heapq as hq

def solution(n, times):
    heap = []
    
    avg = 0
    for t in times :
        avg += 1.0 / t  
    Sum = (1/avg) * n
    
    for i in times :
        cnt = int(Sum) // i
        if cnt <= 0 :
            continue
        hq.heappush(heap, [i*(cnt+1), cnt])
        n -= cnt
    
    answer = heap[0][0] - (heap[0][0] // (heap[0][1] + 1))
    for _ in range(n) :
        cnt, num = hq.heappop(heap)
        answer = cnt
        hq.heappush(heap, [cnt+(cnt//(num+1)), num+1])
    return answer

print(solution(22, [51, 510]))

'''
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
'''