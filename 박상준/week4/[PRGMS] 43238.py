def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    # 가능한 최소 분, 최대 분(제일 느린 사람이 모두 다 처리)
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        for time in times:
            people += mid // time 
            # 심사관들이 중간 시간동안 심사할 수 있는 사람 수들 합치기
            if people >= n: # 더 이상 심사할 사람이 없으면 for문 탈출
                break
        
        if people >= n: 
            # 해당 시간동안 심사 가능한 사람이 n보다 크거나 많으면
            # 이분 탐색 앞
            answer = mid
            right = mid - 1
        elif people < n:
            # 아니면 이분 탐색 뒤
            left = mid + 1
            
    return answer
