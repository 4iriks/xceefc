import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    answer = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        x = a[i]
        while stack and stack[-1] <= x:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(x)

    sys.stdout.write(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()
