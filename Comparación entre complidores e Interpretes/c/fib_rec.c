/* Fibonacci recursivo (naive).
   Propósito: comparar recursión vs iteración y C (compilado) vs Python (interpretado). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

static unsigned long long fib_rec(int n) {
    if (n < 2) return (unsigned long long)n;
    return fib_rec(n-1) + fib_rec(n-2);
}

int main(int argc, char** argv) {
    if (argc < 2) { fprintf(stderr, "uso: fib_rec N\n"); return 1; }
    int n = atoi(argv[1]);
    /* Nota: sin protección de overflow; para uint64, n <= 93. */
    printf("%llu\n", fib_rec(n));
    return 0;
}
