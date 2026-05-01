import sys
from collections import deque


def farthest_vertex(start: int, graph: list[list[int]]) -> tuple[int, int]:
    n = len(graph) - 1
    dist = [0] * (n + 1)
    dist[start] = 1
    queue = deque([start])
    farthest = start

    while queue:
        vertex = queue.popleft()
        farthest = vertex
        for to in graph[vertex]:
            if dist[to] == 0:
                dist[to] = dist[vertex] + 1
                queue.append(to)

    return farthest, dist[farthest]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    graph = [[] for _ in range(n + 1)]
    pos = 1

    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    one_end, _ = farthest_vertex(1, graph)
    _, diameter = farthest_vertex(one_end, graph)
    print(diameter)


if __name__ == "__main__":
    main()
