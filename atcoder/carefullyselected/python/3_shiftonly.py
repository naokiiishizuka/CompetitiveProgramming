from __future__ import annotations

import sys


def count_divisions_by_two(numbers: list[int]) -> int:
    count = 0
    while numbers and all(number % 2 == 0 for number in numbers):
        numbers = [number // 2 for number in numbers]
        count += 1
    return count


def main() -> None:
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    numbers = list(map(int, data[1 : 1 + n]))
    print(count_divisions_by_two(numbers))


if __name__ == "__main__":
    main()
