# Program to print fibonacci sequence without memoization
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


print(fib2(2))