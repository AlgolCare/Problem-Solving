import sys
sys.setrecursionlimit(10**6)
from collections import deque

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int,input())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0
ans = []
    
def bfs():
    queue = deque([0,0])
    visited[0][0] = 1
    cnt = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]  
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny]==0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 0
                    cnt += 1
    ans.append(cnt)
    return cnt

while 1:
    time += 1        
    visited = [[0]*C for _ in range(R)]
    cnt = bfs()
    if cnt == 0 :
        break

print(time-1)
print(ans[-2])