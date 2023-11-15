def solution(n, results):
    answer = n
    graph = [[None] * n for _ in range(n)]

    for n1, n2 in results:
        graph[n1 - 1][n2 - 1] = 1
        graph[n2 - 1][n1 - 1] = -1

    for i in range(n):
        graph[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1

    for row in graph:
        if None in row:
            answer -= 1

    return answer
