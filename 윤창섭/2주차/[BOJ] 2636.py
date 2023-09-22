import sys
from collections import deque

sys.setrecursionlimit(10**6)


class Cheese:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = [list(map(int, input().split())) for i in range(r)]
        self.visited = [[False] * c for i in range(r)]
        self.dy = [-1, 0, 1, 0]
        self.dx = [0, 1, 0, -1]

    def reset_visited(self):
        self.visited = [[False] * self.c for i in range(self.r)]

    def cheese_empty(self):
        return all(cell == 0 for r in self.board for cell in r)

    def find_cheese(self):
        return sum(1 for r in self.board for cell in r if cell == 1)

    def dfs(self, sy, sx):
        if self.board[sy][sx] == 1:
            self.board[sy][sx] = 0
            return

        for i in range(4):
            ny, nx = sy + self.dy[i], sx + self.dx[i]
            if ny < 0 or nx < 0 or ny >= self.r or nx >= self.c or self.visited[ny][nx]:
                continue
            self.visited[ny][nx] = True
            self.dfs(ny, nx)
        return

    def bfs(self, sy, sx):
        queue = deque()
        queue.append([sy, sx])
        self.visited[sy][sx] = True

        while queue:
            y, x = queue.popleft()

            if self.board[y][x] == 1:
                self.board[y][x] = 0
                continue

            for i in range(4):
                ny, nx = y + self.dy[i], x + self.dx[i]

                if (
                    ny < 0
                    or nx < 0
                    or ny >= self.r
                    or nx >= self.c
                    or self.visited[ny][nx]
                ):
                    continue
                self.visited[ny][nx] = True
                queue.append([ny, nx])

    def solve_dfs(self):
        time = 0
        cheese_counts = []

        while True:
            self.reset_visited()
            tmp = self.find_cheese()
            self.dfs(0, 0)
            cheese_counts.append(self.find_cheese())
            time += 1
            if self.cheese_empty():
                cheese_counts.pop()
                break
        return time, cheese_counts[-1] if cheese_counts else tmp

    def solve_bfs(self):
        time = 0
        cheese_counts = []

        while True:
            self.reset_visited()
            tmp = self.find_cheese()
            self.bfs(0, 0)
            cheese_counts.append(self.find_cheese())
            time += 1
            if self.cheese_empty():
                cheese_counts.pop()
                break
        return time, cheese_counts[-1] if cheese_counts else tmp


def main():
    r, c = map(int, input().split())
    board = Cheese(r, c)
    time, cnt = board.solve_bfs()
    print(time, cnt)


main()

"""
함수형으로 풀어본 뒤 해당 로직을 클래스형으로 다시 풀어봤다

우선 dfs와 bfs 모두 사용했다.

dfs는 재귀를 사용했고, bfs는 deque를 사용했다.
dfs의 경우 108ms, bfs의 경우 92ms가 걸렸다

또한 dfs를 사용할 경우, 함수형으로 풀었을 때는 112ms, 클래스형으로 풀었을 때는 108ms가 걸렸고, 코드길이 또한 짧아졌다

"""
