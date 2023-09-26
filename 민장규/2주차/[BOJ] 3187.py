import sys
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
visited = [[False for _ in range(c)] for _ in range(r)]
arr = [list(input()) for _ in range(r)]

def valid(i, j) :
    if i < 0 or j < 0 or i >= r or j >= c or arr[i][j] == "#" or visited[i][j] == True :
        return False
    else :
        return True

def DFS(i, j) :
    global lst
    
    if not valid(i, j) :
        return
    
    visited[i][j] = True
    if arr[i][j] == 'k' :
        lst[0] += 1
    if arr[i][j] == 'v' :
        lst[1] += 1

    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
        DFS(i+dy, j+dx)
        
result = [0, 0]
for i in range(r) :
    for j in range(c) :
        lst = [0, 0]
        DFS(i, j)
        if lst[0] > lst[1] :
            result[0] += lst[0]
        else :
            result[1] += lst[1]
            
for i in result :
    print(i)