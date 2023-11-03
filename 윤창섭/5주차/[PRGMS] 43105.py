def solution(triangle):
    answer = 0
    for i, v in enumerate(triangle):
        tmp = [0] + v + [0]
        triangle[i] = tmp
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    answer = max(triangle[-1])
    return answer