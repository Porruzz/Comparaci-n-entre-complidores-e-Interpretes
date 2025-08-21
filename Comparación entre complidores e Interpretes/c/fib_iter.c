/* Fibonacci iterativo.
   Complejidad: tiempo O(n), memoria O(1). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

static unsigned long long fib_iter(int n) {
    unsigned long long a = 0, b = 1, t;
    for (int i = 0; i < n; ++i) { t = b; b = a + b; a = t; }
    return a;
}

int main(int argc, char** argv) {
    if (argc < 2) { fprintf(stderr, "uso: fib_iter N\n"); return 1; }
    int n = atoi(argv[1]);
    printf("%llu\n", fib_iter(n));
    return 0;
}
