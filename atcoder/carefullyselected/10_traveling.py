from __future__ import annotations

import sys


def is_plan_possible(plan: list[tuple[int, int, int]]) -> bool:
    prev_t, prev_x, prev_y = 0, 0, 0
    for t, x, y in plan:
        dt = t - prev_t
        dist = abs(x - prev_x) + abs(y - prev_y)
        if dist > dt or (dt - dist) % 2 != 0:
            return False
        prev_t, prev_x, prev_y = t, x, y
    return True


def main() -> None:
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    plan: list[tuple[int, int, int]] = []
    for _ in range(n):
        t_str = input().split()
        if not t_str:
            continue
        t, x, y = map(int, t_str)
        plan.append((t, x, y))

    print("Yes" if is_plan_possible(plan) else "No")


if __name__ == "__main__":
    main()
