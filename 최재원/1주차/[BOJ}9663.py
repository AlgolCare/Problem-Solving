def promising(a):
    for i in range(a):
        if board[i] == board[a] or abs(board[i] - board[a]) == abs(i - a):
            return False
    return True

def nqueen(a):
    global cnt
    if a == n:
        cnt += 1
        return
    
    for i in range(n):
        board[a] = i
        if promising(a):
            nqueen(a + 1)

n = int(input())
board = [-1] * 15
cnt = 0
nqueen(0)
print(cnt)
