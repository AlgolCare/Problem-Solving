import sys


def read_line():
    return sys.stdin.readline().strip()


def coordinate(idx, sx, ex, sy, ey):
    """
    param idx:
    param sx, ex: 사분면의 범위가 sx ~ ex
    param sy, ey: 사분면의 범위가 sy ~ ey
    return: 기저사례에서 최종적인 사분면의 좌표 반환
    """

    if d == idx:
        return sx, sy

    half_x = (sx + ex) // 2
    half_y = (sy + ey) // 2

    if arr[idx] == "1":
        return coordinate(idx + 1, half_x, ex, sy, half_y)
    elif arr[idx] == "2":
        return coordinate(idx + 1, sx, half_x, sy, half_y)
    elif arr[idx] == "3":
        return coordinate(idx + 1, sx, half_x, half_y, ey)
    elif arr[idx] == "4":
        return coordinate(idx + 1, half_x, ex, half_y, ey)


def quadrant(sx, ex, sy, ey):
    """
    param sx, ex: 사분면의 범위가 sx ~ ex
    param sy, ey: 사분면의 범위가 sy ~ ey
    return: 기저사례에서 최종적인 사분면 번호 반환
    """

    global answer
    if len(answer) == d:
        return answer

    half_x = (sx + ex) // 2
    half_y = (sy + ey) // 2

    if half_x <= nx < ex and sy <= ny < half_y:
        answer += "1"
        return quadrant(half_x, ex, sy, half_y)
    elif sx <= nx < half_x and sy <= ny < half_y:
        answer += "2"
        return quadrant(sx, half_x, sy, half_y)
    elif sx <= nx < half_x and half_y <= ny < ey:
        answer += "3"
        return quadrant(sx, half_x, half_y, ey)
    elif half_x <= nx < ex and half_y <= ny < ey:
        answer += "4"
        return quadrant(half_x, ex, half_y, ey)


d, q_num = read_line().split()
d = int(d)
x, y = map(int, read_line().split())
arr = [i for i in q_num]

n = 1 << d  # 2^d

dx, dy = coordinate(0, 0, n, 0, n)
nx, ny = dx + x, dy - y

answer = ""

if 0 <= nx < n and 0 <= ny < n:
    print(int(quadrant(0, n, 0, n)))
else:
    print(-1)