from __future__ import annotations


def main() -> None:
    parts = ["dreamer", "eraser", "dream", "erase"]

    s = input().strip()
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for idx in range(len(s)):
        if not dp[idx]:
            continue
        for part in parts:
            end = idx + len(part)
            if end <= len(s) and s[idx:end] == part:
                dp[end] = True

    print("YES" if dp[len(s)] else "NO")


if __name__ == "__main__":
    main()
