from collections import deque


def bfs(graph, root):
    visited = {node: -1 for node in graph}  # Graph의 모든 node에 대해 depth를 -1로 초기화
    queue = deque([(root, 0)])  # Deque: [node, depth]

    while queue:
        current_node, depth = queue.popleft()
        if visited[current_node] == -1:  # 방문하지 않은 점에 대해
            visited[current_node] = depth  # 현재 깊이를 저장
            for neighbor in graph[current_node]:  # 현재 노드의 다음 노드에 대해
                if visited[neighbor] == -1:  # 방문하지 않았다면
                    queue.append((neighbor, depth + 1))  # 깊이를 늘려 방문

    return visited


def solution(n, edge):
    graph = dict()
    for a, b in edge:  # 주어진 리스트를 dict형태로 변환 -> graph 형태로 나타낼 수 있음
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    depths = bfs(graph, 1)
    max_depth = max(depths.values())

    return list(depths.values()).count(max_depth)


"""
깊이를 구하여, 가장 큰 깊이가 몇 개 존재하는 지 구하면 되는 문제
처음에 dfs를 쓰려고 했지만, dfs를 쓸 경우 레벨별 탐색이 가능하지 않아 bfs를 사용하여 해결
dfs의 경우 한 방향으로만 탐색을 하기 때문에, 레벨별 탐색이 불가능함
bfs의 경우 시작 정점으로부터 가까운 노드부터 탐색함. 즉, 레벨별 탐색이 가능함
"""
