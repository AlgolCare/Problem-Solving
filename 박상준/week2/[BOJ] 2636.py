from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i, j in zip(dx, dy):
            if x + i < 0 or x + i >= n or y + j < 0 or y + j >= m:
                continue
            if graph[x + i][y + j] == 0 and visited[x + i][y + j] == 0:
                queue.append((x + i, y + j))
                visited[x + i][y + j] = 1
            if graph[x + i][y + j] == 1:
                visited[x + i][y + j] = 1
                graph[x + i][y + j] = 0


def remaining_cheese():
    sum = 0
    for i in range(n):            
        sum += graph[i].count(1)
    return sum


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

hour = 0
bf = 0
while True:
    hour += 1
    bf = remaining_cheese()
    bfs()
    at = remaining_cheese()
    if at == 0:
        break
    bf = at

print(hour)
print(bf)
