def solution(n, results):
    answer = 0
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(results)):
        arr[results[i][0]-1][results[i][1]-1] = 1
        arr[results[i][1]-1][results[i][0]-1] = -1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[j][i] == 1 and arr[i][k] == 1:
                    arr[j][k] = 1
                    arr[k][j] = -1
    for i in range(n):
        if arr[i].count(0) == 1:
            answer += 1
    return answer