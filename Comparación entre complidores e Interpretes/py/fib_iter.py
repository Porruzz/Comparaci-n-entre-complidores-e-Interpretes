# Fibonacci iterativo: O(n) tiempo, O(1) memoria.
import sys

def fib_iter(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("uso: python fib_iter.py N"); raise SystemExit(1)
    n = int(sys.argv[1])
    print(fib_iter(n))
