from __future__ import annotations


def main() -> None:
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    unique_sizes = set(numbers)

    print(len(unique_sizes))


if __name__ == "__main__":
    main()
