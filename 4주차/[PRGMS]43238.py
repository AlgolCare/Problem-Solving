def solution(n, times):
    
    times.sort()
    answer = 0
    min = times[0]
    max = times[0] * n
    while(1):
        count = 0
        mid = ( min + max )//2
        for i in times:
            count +=( mid//i )
        if( count >= n ):
            max = mid
        elif( count < n ):
            min = mid
        if( min == max-1 ):
            answer = max
            break

    return answer

solution(6, [7, 10])
print(solution(6, [7, 10]))