from collections import deque


def solution(n, edge):
    v_map = [[]for _ in range(n)]
    
    for item in edge: # 맵 만들기
        v_map[item[0] - 1].append(item[1] - 1)
        v_map[item[1] - 1].append(item[0] - 1)
        
    visited = [999 for _ in range(n)]
    visited[0] = 0 # 본인까지의 cost는 0
    queue = deque()
    queue.append(0) 
        
    while queue:
        current_v = queue.popleft()
        for v in v_map[current_v]:
            if visited[v] == 999 or visited[v] > visited[current_v] + 1:
                visited[v] = visited[current_v] + 1
                queue.append(v)
        
    answer = visited.count(max(visited))
    return answer
