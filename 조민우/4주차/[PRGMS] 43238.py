import sys
sys.setrecursionlimit(10**6)
def find(time, first, last, n):
    if (first == last - 1):
        return last
    else:
        mid = (first + last) // 2
        sum = 0
        for i in range(len(time)):
            sum += mid // time[i]
        if sum >= n:
            return find(time, first, mid, n)
        else:
            return find(time, mid, last, n)

def solution(n, times):
    answer = 0
    first = min(times) * (n // len(times))
    last = max(times) * (n // len(times))
    answer = find(times, first, last, n)
    return answer
