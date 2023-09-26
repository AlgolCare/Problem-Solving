def find(r, dic, visited) :
    lst = []
    for i in dic[r] :
        if not visited[i] :
            visited[i] = True
            lst.append(i)
    return lst
        
def solution(n, edge):
    dic = {}
    visited = [False for _ in range(n)]
    visited[0] = True
    
    for i, j in edge :
        i -= 1
        j -= 1
        if i not in dic :
            dic[i] = [j]
        elif i in dic :
            dic[i].append(j)
        if j not in dic :
            dic[j] = [i]
        elif j in dic :
            dic[j].append(i)
        
    r = [0]
    while True :
        lst = []
        for i in r :
            lst.extend(find(i, dic, visited))
        
        if len(lst) == 0 :
            return len(r)
        
        r = lst.copy()
        
'''
def find(r, n, arr, visited) :
    lst = []
    
    for c in range(n) :
        if arr[r][c] and not visited[c] :
            visited[c] = True
            lst.append(c)
    return lst
        
def solution(n, edge):
    arr = [[False for _ in range(n)] for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[0] = True
    
    for i, j in edge :
        arr[i-1][j-1] = True
        arr[j-1][i-1] = True
        
    r = [0]
    while True :
        lst = []
        for i in r :
            lst.extend(find(i, n, arr, visited))
        
        if len(lst) == 0 :
            return len(r)
        
        r = lst.copy()
'''