n, m = map(int, input().split())
board = [list(input()) for i in range(n)]
count = []

for i in range(n - 7):
    for j in range(m - 7):
        white = 0
        black = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "W":
                        white += 1
                    if board[a][b] != "B":
                        black += 1
                else:
                    if board[a][b] != "B":
                        white += 1
                    if board[a][b] != "W":
                        black += 1
        count.append(white)
        count.append(black)
print(min(count))

"""
첫 번쨰 칸이 B일 경우 
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB

첫 번째 칸이 W일 경우
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

이 두 경우 뿐이다.

보드판을 8 x 8로 분해한다.

분해한 각 보드판의 요소를 분석한다.
white의 경우 첫 번째 칸이 W일 경우, black의 경우 첫 번째 칸이 B일 경우의 수정해야 하는 칸의 개수이다.
"""
