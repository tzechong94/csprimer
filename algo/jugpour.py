"""
state transitions
- empty L (a,b) -> (0,b)
- empty R (a,b) -> (a,0)
- fill L (a,b) -> (3, b)
- fill R (a,b) -> (a, 5)
- transfer LR (a,b) -> (max(0, a+b-5), min(5, a+b))
- transfer RL (a,b) -> (min(3, a+b), max(0, a+b-3)
"""

from collections import deque


def solve(left, right, goal):
    q = deque()
    q.append(((0, 0), []))  # a , b , depth
    visited = set()
    while q:
        (a, b), ops = q.popleft()
        if a == goal or b == goal:
            return ops
        candidates = (
            ((0, b), "empty left"),
            ((a, 0), "empty right"),  # empty L or R
            ((left, b), "fill left"),
            ((a, right), " fill right"),  # fill L or R
            (
                (max(0, a + b - right), min(right, a + b)),
                "transfer L -> R",
            ),  # transfer L to R
            ((min(left, a + b), max(0, a + b - left)), "transfer right to left"),
        )
        for c, op in candidates:
            if c not in visited:
                q.append((c, ops + [op]))
                visited.add(c)

    return -1


if __name__ == "__main__":
    print(solve(3, 5, 4))
