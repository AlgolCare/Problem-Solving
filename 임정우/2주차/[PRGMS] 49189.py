from collections import deque

def solution(n, edge):
    visited = [0]*(n+1)
    dq = deque([1])
    visited[1] = 1
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    while dq:
        now = dq.popleft()
        
        for adj_node in graph[now]:
            if not visited[adj_node]:
                visited[adj_node] =  visited[now] + 1
                dq.append(adj_node)
    
    return visited.count(max(visited))