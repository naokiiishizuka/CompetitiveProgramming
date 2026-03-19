from __future__ import annotations


def can_construct(target: str) -> bool:
    parts = ["dreamer", "eraser", "dream", "erase"]
    reversed_parts = [p[::-1] for p in parts]
    reversed_target = target[::-1]

    idx = 0
    length = len(reversed_target)
    while idx < length:
        matched = False
        for part in reversed_parts:
            if reversed_target.startswith(part, idx):
                idx += len(part)
                matched = True
                break
        if not matched:
            return False
    return True


def main() -> None:
    s = input().strip()
    print("YES" if can_construct(s) else "NO")


if __name__ == "__main__":
    main()
