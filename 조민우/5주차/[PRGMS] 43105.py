def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            first = max(0, j-1)
            last = min(j, len(triangle[i-1])-1)
            triangle[i][j] += max(triangle[i-1][first],triangle[i-1][last])
    answer = max(triangle[len(triangle)-1])
    return answer