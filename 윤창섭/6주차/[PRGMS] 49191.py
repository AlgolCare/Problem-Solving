def solution(n, results):
    answer = 0
    # dist를 무한대로 초기화
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    # 각 정점에서 자기 자신으로 가는 비용은 0
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    # 가중치가 정해지지 않았으므로 모두 1로 초기화
    for src, dst in results:
        dist[src][dst] = 1
    

    # 플로이드 와샬 알고리즘 사용
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if i == k: # 출발지 == 경유지인 경우 비교할 필요가 없음
                continue
            for j in range(1, n + 1):
                if i == j: # 출발지 == 도착지인 경우 비교할 필요가 없음
                    continue
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    

    # 아래 알고리즘 보다 경유 효과가 없는 경우를 제외한 위의 알고리즘이 더 빠름
    # for k in range(1, n + 1):
    #     for i in range(1, n + 1):
    #         for j in range(1, n + 1):
    #             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
    # 서로 연결된 정점에 대해서 dist[i][j]와 dist[j][i]가 모두 무한대가 아니라면 연결되어 있다고 판단
    for i in range(1, n + 1):
        connected = True
        for j in range(1, n + 1):
            if i != j and dist[i][j] == float('inf') and dist[j][i] == float('inf'):
                connected = False
                break
        if connected:
            answer += 1

    return answer
