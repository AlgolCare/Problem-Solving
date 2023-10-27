"""
프로그래머스 입국심사

구현
- 입국심사에 걸리는 최소시간과 최대시간 탐색
- 최소시간: n = 1이고, 심사관이 입국심사에 1분이 걸리는 경우 -> 1
- 최대시간: 입국심사에 걸리는 최대시간 * n
- 해당 최소시간과 최대시간에서 이분탐색을 진행
- 중앙값을 정하고 times를 순회하며 해당 중앙값 / time을 통해 해당 시간동안 심사받을 수 있는 사람 수 탐색
- 심사받을 수 있는 사람이 n보다 작다면 최소시간 + 1
- 그 외 최대시간 - 1

알고리즘
- 이분탐색
"""


def solution(n, times):
    answer = 1
    min_time = 1
    max_time = max(times) * n
    times.sort()  # 정렬된 값인지 모르기 때문에 정렬

    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:  # 시간을 줄이기 위해 이미 넘는경우 break
                break
        if people < n:
            min_time = mid + 1
        else:
            answer = mid
            max_time = mid - 1
    return answer
