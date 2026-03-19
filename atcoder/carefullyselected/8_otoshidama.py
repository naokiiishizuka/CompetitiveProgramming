from __future__ import annotations


def main() -> None:
    N, Y = map(int, input().split())

    for x in range(N + 1):
        for y in range(N - x + 1):
            z = N - x - y

            total = 10000 * x + 5000 * y + 1000 * z
            if total == Y:
                print(x, y, z)
                return

    print(-1, -1, -1)


if __name__ == "__main__":
    main()
