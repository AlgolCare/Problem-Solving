n = int(input())
board = [0] * (n+1)
count = 0
def check(cnt):
    for i in range(1, cnt):
        if (board[cnt] == board[i] or abs(board[cnt] - board[i]) == cnt - i):
            return False
    return True
def find(cnt):
    if (cnt == n+1):
        global count
        count += 1
        return
    for i in range(1, n+1):
        board[cnt] = i
        if (check(cnt)):
            find(cnt + 1)
find(1)
print(count)