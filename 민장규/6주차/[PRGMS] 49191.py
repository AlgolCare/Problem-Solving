def solution(n, results):
    answer = 0
    INF = 1000000
    
    rank = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        rank[i][i] = 0
        
    for i in results :
        win = i[0] - 1
        lose = i[1] - 1
        rank[win][lose] = 1
        
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                rank[i][j] = min(rank[i][j], rank[i][k] + rank[k][j])
    
    for i in range(n) :
        canRank = True
        for j in range(n) :
            if rank[i][j] == INF and rank[j][i] == INF :
                canRank = False
                break
        if canRank :
            answer += 1
    
    return answer