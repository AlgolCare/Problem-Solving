import heapq

INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
test = 1

while True:
    n = int(input())
    
    if n == 0:
        break

    distance = [[INF]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, input().split()))
        
    def dijkstra(y, x):
        q = []
        distance[y][x] = graph[0][0]
        heapq.heappush(q, (graph[0][0], y, x))

        while q:
            dist, row, col = heapq.heappop(q)
            if distance[row][col] < dist:
                continue
            for d in range(4):
                r = row + dy[d]
                c = col + dx[d]
                if -1 < r < n and -1 < c < n and distance[r][c] > graph[r][c] + dist:
                    distance[r][c] = dist + graph[r][c]
                    heapq.heappush(q, (distance[r][c], r, c))

    dijkstra(0, 0)
    print(f'Problem {test}: {distance[n-1][n-1]}')
    test += 1
