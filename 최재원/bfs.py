from collections import deque

def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = True
    
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True

graph = [
    [],
    [2, 3, 8], 
    [1, 7], 
    [1, 4, 5], 
    [3, 5], 
    [3, 4], 
    [7], 
    [2, 6, 8], 
    [1, 7]
]

visit = [False] * 9

bfs(graph, 1, visit)