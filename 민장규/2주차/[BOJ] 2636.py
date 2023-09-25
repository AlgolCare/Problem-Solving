import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c = map(int, input().split())
arr = []
for _ in range(r) :
    cnt = list(map(int, input().split()))
    cnt.insert(0, 0)
    cnt.append(0)
    arr.append(cnt)
arr.insert(0, [0 for _ in range(c+2)])
arr.append([0 for _ in range(c+2)])
visited = [[False for _ in range(c+2)] for _ in range(r+2)]

def valid(i, j) :
    global cheese, visited, arr
    
    if i < 0 or j < 0 or i >= r+2 or j >= c+2 or visited[i][j] == True :
        return False
    elif arr[i][j] == 1 :
        visited[i][j] = True
        cheese.append([i, j])
        return False
    else :
        return True
    
def DFS(i, j) :
    global visited
    
    if not valid(i, j) :
        return
    
    visited[i][j] = True
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]] :
        DFS(i+dy, j+dx)

count = 0
for i in range(r+2) :
    for j in range(c+2) :
        if arr[i][j] == 1 :
            count += 1

hour = 0
while True :
    cheese = []    
    DFS(0, 0)
    
    if count == len(cheese) :
        print(hour+1)
        print(len(cheese))
        exit()
        
    for i, j in cheese :
        arr[i][j] = 0
    hour += 1
    count -= len(cheese)
    visited = [[False for _ in range(c+2)] for _ in range(r+2)]