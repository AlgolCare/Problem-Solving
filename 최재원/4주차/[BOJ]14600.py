import sys


def read_line():
    return sys.stdin.readline().strip()


def check(x, y, size):
    """
    return: 트로미노가 채워지지 않은 경우 True
    """
    for nx in range(x, x + size):
        for ny in range(y, y + size):
            if answer[nx][ny] != 0:
                return False
    return True


def tromino(x, y, size):
    global num
    num += 1
    half = size // 2
    pos = [
        [x + half - 1, y + half - 1],
        [x + half, y + half - 1],
        [x + half - 1, y + half],
        [x + half, y + half],
    ]  # 분할된 사각형의 좌표

    # index와 value 함께 순회
    for idx, val in enumerate(
        [[x, y], [x + half, y], [x, y + half], [x + half, y + half]]
    ):
        sx, sy = val
        ix, iy = pos[idx]
        if check(sx, sy, half):
            answer[ix][iy] = num

    if size == 2:
        return

    tromino(x, y, half)
    tromino(x + half, y, half)
    tromino(x, y + half, half)
    tromino(x + half, y + half, half)


n = 1 << int(read_line())
x, y = map(int, read_line().split())
answer = [[0 for i in range(0, n)] for i in range(0, n)]
answer[n - y][x - 1] = -1  # y축을 반대로 셈

num = 0
tromino(0, 0, n)

for row in answer:
    print(*row)