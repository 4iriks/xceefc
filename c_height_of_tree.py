import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    if n == 1:
        print(1)
        return

    children = [[] for _ in range(n + 1)]
    for vertex, parent in enumerate(data[1:], start=2):
        children[parent].append(vertex)

    height = 0
    stack = [(1, 1)]
    while stack:
        vertex, depth = stack.pop()
        if depth > height:
            height = depth
        for child in children[vertex]:
            stack.append((child, depth + 1))

    print(height)


if __name__ == "__main__":
    main()
