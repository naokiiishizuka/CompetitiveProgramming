from __future__ import annotations


def sum_of_digits(number: int) -> int:
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


def main() -> None:
    n, a, b = map(int, input().split())
    result = 0
    for i in range(n + 1):
        sum = sum_of_digits(i)
        if sum >= a and sum <= b:
            result += i
    print(result)


if __name__ == "__main__":
    main()
