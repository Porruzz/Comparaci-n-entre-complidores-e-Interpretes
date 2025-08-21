# Fibonacci recursivo (naive). Se sube el límite de recursión por seguridad.
import sys
sys.setrecursionlimit(1_000_000)

def fib_rec(n: int) -> int:
    return n if n < 2 else fib_rec(n-1) + fib_rec(n-2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("uso: python fib_rec.py N"); raise SystemExit(1)
    n = int(sys.argv[1])
    print(fib_rec(n))
