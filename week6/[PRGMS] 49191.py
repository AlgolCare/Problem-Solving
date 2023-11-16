def solution(n, results):
    answer = 0
    battle_graph = [[0] * n for _ in range(n)]
    
    for result in results:
        battle_graph[result[0] - 1][result[1] - 1] = 1
        battle_graph[result[1] - 1][result[0] - 1] = -1
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == k or battle_graph[j][k] in [1,-1]:
                    continue
                if battle_graph[j][i] == battle_graph[i][k] == 1:
                    battle_graph[j][k] = 1
                    battle_graph[k][j] = battle_graph[i][j] = battle_graph[k][i] = -1
                    
    for battle in battle_graph:
        if battle.count(0) == 1:
            answer += 1

    return answer