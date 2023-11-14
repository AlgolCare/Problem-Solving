import sys

def read_line():
    return sys.stdin.readline()

# edge 클래스
class Edge():
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

n, m = map(int, read_line().split())
edges = []
for i in range(m):
    a, b, c = map(int, read_line().split())
    edges.append(Edge(a, b, c))

# 1번 노드에서 다른 노드로 가는 최소 비용을 담는 배열
dist = [float('inf') for i in range(n + 1)]
dist[1] = 0

# 최대 n개의 정점을 가지기 때문에 n-1번의 완화 과정을 반복
# 완화 과정은 dist 배열의 값이 갱신되는 경우 발생함
for i in range(n - 1):
    for edge in edges:
        if dist[edge.src] != float('inf') and dist[edge.dest] > dist[edge.src] + edge.weight:
            dist[edge.dest] = dist[edge.src] + edge.weight

# n-1번의 완화 과정을 반복한 후에도 완화가 발생한다면 음수 사이클이 존재함 -> -1 출력
for edge in edges:
    if dist[edge.src] != float('inf') and dist[edge.dest] > dist[edge.src] + edge.weight:
        print(-1)
        exit()

# 음수 사이클이 존재하지 않는다면 2번 노드부터 n번 노드까지의 최소 비용 출력 -> 1번 노드는 이미 0으로 초기화되어 있음
for i in range(2, n + 1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])
