import sys
import heapq

def read_line():
    return sys.stdin.readline()

idx = 1

def dijkstra(board):
    rows, cols = len(board), len(board[0])
    # 최소 비용을 담는 2차원 배열 -> 모두 무한대로 초기화
    dist = [[float('inf') for i in range(cols)] for j in range(rows)]
    dist[0][0] = board[0][0]

    # 우선순위 큐에 비용, 행, 열을 담음
    pq = [(board[0][0], 0, 0)]

    while pq:
        cost, row, col = heapq.heappop(pq)

        # 마지막 칸에 도달했을 경우
        if row == rows - 1 and col == cols - 1:
            return cost
        
        # 각 칸에 대해 상하좌우로 이동
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            r, c = row + dr, col + dc
            # 범위 내에 있고, 현재 칸까지의 비용 + 다음 칸의 비용이 최소 비용보다 작을 경우
            if 0 <= r < rows and 0 <= c < cols:
                if dist[r][c] > cost + board[r][c]:
                    dist[r][c] = cost + board[r][c]
                    heapq.heappush(pq, (dist[r][c], r, c))
    # 마지막 칸에 대한 최소 비용 반환
    return dist[rows - 1][cols - 1]

while True:
    n = int(read_line())
    if n == 0:
        break
    board = [list(map(int, read_line().split())) for i in range(n)]
    print(f'Problem {idx}: {dijkstra(board)}')
    idx += 1
