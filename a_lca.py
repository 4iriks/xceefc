import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    parents = data[1:n]
    q_index = n
    q = data[q_index]
    queries = data[q_index + 1:]

    log = max(1, n.bit_length())
    up = [[0] * (n + 1) for _ in range(log)]
    depth = [0] * (n + 1)

    up[0][1] = 1
    for vertex in range(2, n + 1):
        parent = parents[vertex - 2]
        up[0][vertex] = parent
        depth[vertex] = depth[parent] + 1

    for level in range(1, log):
        previous = up[level - 1]
        current = up[level]
        for vertex in range(1, n + 1):
            current[vertex] = previous[previous[vertex]]

    def lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u

        difference = depth[u] - depth[v]
        bit = 0
        while difference:
            if difference & 1:
                u = up[bit][u]
            difference >>= 1
            bit += 1

        if u == v:
            return u

        for level in range(log - 1, -1, -1):
            if up[level][u] != up[level][v]:
                u = up[level][u]
                v = up[level][v]

        return up[0][u]

    answer = []
    for i in range(q):
        u = queries[2 * i]
        v = queries[2 * i + 1]
        answer.append(str(lca(u, v)))

    sys.stdout.write("\n".join(answer))


if __name__ == "__main__":
    main()
