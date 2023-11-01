def solution(n, edge):
    answer = 0
    map = [[] for i in range(n+1)]
    visit = [0 for i in range(n+1)]
    for i in range(len(edge)):
        map[edge[i][0]].append(edge[i][1])
        map[edge[i][1]].append(edge[i][0])
    queue = [1]
    visit[1] = 1
    while(queue):
        x = queue[0]
        queue.pop(0)
        for i in map[x]:
            if visit[i] == 0:
                visit[i] = visit[x] + 1
                queue.append(i)
    answer = visit.count(max(visit))
    return answer