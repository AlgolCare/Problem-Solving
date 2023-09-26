from collections import deque

def solution(n, edge) :
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    graph = [[] for _ in range(n+1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = visited[v] + 1
    
    max_distance = max(visited)
    return visited.count(max_distance)
                
        
solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
    
