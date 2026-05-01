import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    parent = [0] * (n + 1)
    children: list[list[int]] = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        p = int(data[idx]); idx += 1
        parent[i] = p
        children[p].append(i)

    depth = [1] * (n + 1)
    order = [1]
    head = 0
    best = 1
    while head < len(order):
        v = order[head]
        head += 1
        d = depth[v]
        if d > best:
            best = d
        for c in children[v]:
            depth[c] = d + 1
            order.append(c)
    sys.stdout.write(f"{best}\n")


if __name__ == "__main__":
    main()
