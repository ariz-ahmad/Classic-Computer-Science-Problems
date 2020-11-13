# used memoization : python dictionary
from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]


if __name__ == "__main__":
    print(fib3(6))
