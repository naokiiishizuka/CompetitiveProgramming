from __future__ import annotations


def main() -> None:
    digits = input()
    result = 0

    for digit in digits:
        if digit == "1":
            result += 1

    print(result)


if __name__ == "__main__":
    main()
