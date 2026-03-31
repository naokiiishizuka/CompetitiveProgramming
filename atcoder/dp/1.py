def main() -> None:
    n = int(input())
    numberList = list(map(int, input().split()))

    result = [0 for _ in range(n)]
    for i in range(n):
        if i == 0:
            result[i] = max(0, numberList[i])
            continue
        result[i] = max(result[i - 1] + numberList[i], result[i - 1])

    print(result[-1])


if __name__ == "__main__":
    main()
