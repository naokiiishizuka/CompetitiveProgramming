from __future__ import annotations


def main() -> None:
    n = input()
    numbers = list(map(int, input().split()))

    sortedNumbers = sorted(numbers, reverse=True)

    alice, bob = 0, 0
    for index, num in enumerate(sortedNumbers):
        if index % 2 == 0:
            alice += num
        else:
            bob += num
    print(alice - bob)


if __name__ == "__main__":
    main()
