import sys
from collections import deque


def bfs_farthest(start: int, adj: list[list[int]], n: int) -> tuple[int, int]:
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    far_node = start
    far_dist = 0
    while q:
        v = q.popleft()
        d = dist[v]
        if d > far_dist:
            far_dist = d
            far_node = v
        for u in adj[v]:
            if dist[u] == -1:
                dist[u] = d + 1
                q.append(u)
    return far_node, far_dist


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    adj: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)

    if n == 1:
        sys.stdout.write("1\n")
        return

    a, _ = bfs_farthest(1, adj, n)
    _, d = bfs_farthest(a, adj, n)
    sys.stdout.write(f"{d + 1}\n")


if __name__ == "__main__":
    main()
