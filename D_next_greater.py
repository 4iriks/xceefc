import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    res = [-1] * n
    stack: list[int] = []
    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            res[stack.pop()] = a[i]
        stack.append(i)
    sys.stdout.write(" ".join(map(str, res)))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
