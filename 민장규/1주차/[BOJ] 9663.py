N = int(input())
queen = [[i, -1] for i in range(N)]
result = 0

def Nqueen(r) :
    global result
    
    if r == N :
        result += 1
        return
    
    for i in range(N) :
        queen[r][1] = i
        if findindex(r) :
            Nqueen(r+1)

def left(i, j) :
    return i + j

def right(i, j) :
    return i + (N-1)-j

def findindex(row) :
    for i in range(row) :
        if queen[row][1] == queen[i][1] or left(row, queen[row][1]) == left(queen[i][0], queen[i][1]) or right(row, queen[row][1]) == right(queen[i][0], queen[i][1]) :
            return False
    return True
    
Nqueen(0)
print(result)