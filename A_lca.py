import sys
from sys import setrecursionlimit


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1

    LOG = max(1, (n).bit_length())
    parent = [0] * (n + 1)
    parent[1] = 1
    for i in range(2, n + 1):
        parent[i] = int(data[idx]); idx += 1

    children = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        children[parent[v]].append(v)

    depth = [0] * (n + 1)
    order = [0] * n
    head = 0
    tail = 0
    order[0] = 1
    tail = 1
    while head < tail:
        v = order[head]
        head += 1
        d = depth[v]
        for c in children[v]:
            depth[c] = d + 1
            order[tail] = c
            tail += 1

    up = [parent[:]]
    for _ in range(1, LOG):
        prev = up[-1]
        cur = [prev[p] for p in prev]
        up.append(cur)

    q = int(data[idx]); idx += 1
    out = []
    for _ in range(q):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        k = 0
        while diff:
            if diff & 1:
                u = up[k][u]
            diff >>= 1
            k += 1
        if u != v:
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            u = up[0][u]
        out.append(str(u))
    sys.stdout.write("\n".join(out))
    if out:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
