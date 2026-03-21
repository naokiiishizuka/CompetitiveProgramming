from __future__ import annotations


def main() -> None:
    fiveHundred = 500
    oneHubdred = 100
    fifty = 50

    fiveHundredTotal = int(input())
    oneHubdredTotal = int(input())
    fiftyTotal = int(input())
    sum = int(input())

    result = 0

    for fiveHundredNum in range(fiveHundredTotal + 1):
        for oneHubdredNum in range(oneHubdredTotal + 1):
            for fiftyNum in range(fiftyTotal + 1):
                if (
                    sum
                    == fiveHundred * fiveHundredNum
                    + oneHubdred * oneHubdredNum
                    + fifty * fiftyNum
                ):
                    result += 1
    print(result)


if __name__ == "__main__":
    main()
