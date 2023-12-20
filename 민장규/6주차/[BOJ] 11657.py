import sys
input = sys.stdin.readline

INF = float("inf")
V, E = map(int, input().split())
dis = [INF for _ in range(V)]
dis[0] = 0

edge = []
for _ in range(E) :
    edge.append(list(map(int, input().split())))

circle = []
for i in range(V) :
    for e in edge :
        start = e[0] - 1
        end = e[1] - 1
        cost = e[2]
        
        if dis[start] + cost < dis[end] :
            dis[end] = dis[start] + cost
            
    if i == V - 1 :
        for e in edge :
            start = e[0] - 1
            end = e[1] - 1
            cost = e[2]
            
            if dis[start] + cost < dis[end] :
                circle.append(end)
                dis[end] = dis[start] + cost
            
if len(circle) != 0 :
    print(-1)
    exit()

for i in dis[1:] :
    if i == INF :
        print(-1)
    else :
        print(i)