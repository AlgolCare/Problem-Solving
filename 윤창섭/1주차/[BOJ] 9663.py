n = int(input())

board = [0 for i in range(n)]  # n 크기의 리스트 생성
cnt = 0


def check(i):
    for j in range(i):
        if board[i] == board[j] or abs(board[i] - board[j]) == (i - j):
            return False
    return True


def solve(i):
    if i == n:
        global cnt
        # print(board)
        cnt += 1
        return
    else:
        for j in range(n):
            board[i] = j
            if check(i):
                solve(i + 1)


solve(0)
print(cnt)


"""
queen은 가로, 세로, 대각선으로 움직일 수 있다.
따라서 서로 공격할 수 없게 하려면, 가로, 세로, 대각선에 queen이 없어야 한다.

만약 n이 4인 경우
0 q 0 0
0 0 0 q
q 0 0 0
0 0 q 0

이를 하나의 리스트로 나타내면 다음과 같다.
[2, 4, 1, 3]

이 때, 각 인덱스는 보드판의 열을 의미하고, 각 인덱스의 값은 행을 의미한다.
다음과 같은 리스트는 여러 개 존재할 수 있다.
"""
