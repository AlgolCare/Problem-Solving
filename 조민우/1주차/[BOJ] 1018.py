n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
def find():
    sum = 64
    for k in range(n-7):
        for l in range(m - 7):
            temp = 0
            for i in range(k, k+8):
                for j in range(l, l+8):
                    if (((i + j) % 2 == 0 and board[i][j] == 'B') or ((i + j) % 2 == 1 and board[i][j] == 'W')):
                        temp += 1
            temp = min(temp, 64 - temp)
            sum = min(temp, sum)
    return min(sum, 64-sum)
print(find())