import heapq

question_num = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solve(cave, n):
    distance = [[int(1e9)] * n for _ in range(n)]
    x, y = 0, 0
    queue = [(cave[x][y], x, y)]
    distance[x][y] = cave[x][y]

    while queue:
        dist, x, y = heapq.heappop(queue)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + cave[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(queue, (cost, nx, ny))

    return distance[n-1][n-1]

while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]

    print(f"Problem {question_num}: {solve(cave, n)}")
    question_num += 1