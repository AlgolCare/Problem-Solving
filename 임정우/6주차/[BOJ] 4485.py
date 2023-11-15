from collections import deque

y_ar = [0, 0, -1, 1]
x_ar = [1, -1, 0, 0]

def bfs():
    pq = deque()
    pq.append((0, 0))
    dist[0][0] = arr[0][0]

    while pq:
        y, x = pq.popleft()

        for i in range(4):
            ny = y + y_ar[i]
            nx = x + x_ar[i]

            if 0 <= ny < n and 0 <= nx < n:
                if dist[ny][nx] > dist[y][x] + arr[ny][nx]:
                    dist[ny][nx] = dist[y][x] + arr[ny][nx]
                    pq.append((ny, nx))

cnt = 1

while True:
    n = int(input())
    if n == 0:
        break

    arr = []
    dist = [[2000000000] * n for _ in range(n)]

    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)

    bfs()
    print(f"Problem {cnt}: {dist[n - 1][n - 1]}")
    cnt += 1
