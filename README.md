Comparativa Compilado vs Interpretado 

C vs Python — Fibonacci iterativo y recursivo

La idea es comparar tiempo y memoria entre un lenguaje compilado (C) y uno interpretado (Python) resolviendo el mismo problema con dos sabores: recursivo y iterativo.
Escogí Fibonacci porque muestra clarito el costo de la recursión naive (explota en llamadas) frente a la iteración que es lineal y baratita.


📦 ¿Qué trae este repo?
comparativa-compilado-vs-interpretado/
  .vscode/
    launch.json        # Run & Debug listo para bench y plots
    tasks.json         # Build C en un clic (MSVC o MinGW)
  c/
    fib_rec.c          # Fibonacci recursivo (naive) en C
    fib_iter.c         # Fibonacci iterativo en C (O(n), O(1))
    build_msvc.bat     # Compila con cl.exe (Visual Studio Build Tools)
    build_mingw.bat    # Compila con gcc (MinGW-w64)
    bin/               # Aquí salen los .exe
  py/
    fib_rec.py         # Fibonacci recursivo en Python
    fib_iter.py        # Fibonacci iterativo en Python
    bench.py           # Corre todo, mide tiempo/memoria, guarda results.csv
    plot.py            # Grafica con matplotlib (PNG en figs/)
  figs/                # Imágenes generadas (tiempo/memoria)
  requirements.txt     # psutil + matplotlib
  README.md            # Este documento (con toda la jugada)


🧠 ¿Por qué Fibonacci y no factorial?

Con factorial, recursión e iteración se parecen mucho y no se ve la diferencia tan fuerte.

Con Fibonacci recursivo naive la cosa se pone seria: la cantidad de llamadas crece casi exponencial, y ahí la pila y el overhead del lenguaje se sienten de verdad.

La versión iterativa es O(n) y O(1) memoria. Ideal para comparar “lo que debe ser” vs “lo que no conviene”.

En Windows, MSVC no aplica TCO (tail call optimization) por default y Python tampoco; entonces la comparación es sincera, sin “magia” debajo.

🛠️ Requisitos 

VS Code con extensiones:

Python (ms-python.python)

C/C++ (ms-vscode.cpptools)

Python 3.10+ (de python.org).

Compilador C:

MSVC (Visual Studio Build Tools) o

MinGW-w64 (gcc en Windows).

🚀 Cómo correr todo en 3 pasos (sin abrir cmd)

Instalar paquetes de Python

Abre requirements.txt en VS Code y acepta instalar psutil y matplotlib en tu entorno.

Si no te sale el prompt, crea/selecciona el entorno abajo a la derecha (barra de estado).

Compilar C

VS Code → Terminal → Run Build Task…

Elige C: build (MSVC) (o C: build (MinGW) si usas gcc).

Te deberían salir c/bin/fib_iter.exe y c/bin/fib_rec.exe.

Correr benchmark

VS Code → Run and Debug (F5) → Python: Bench.

Se genera results.csv y automáticamente se dibujan las gráficas en figs/:

time_vs_n.png

mem_vs_n.png

🔬 Metodología 

Cada variante corre como proceso 

Tiempo: se toma con time.perf_counter() alrededor del proceso hijo.

Memoria: muestreamos con psutil la RSS pico (~cada 2 ms). No es un profiler NASA, pero sirve para comparar entre variantes.

Integridad: capturamos el resultado (última línea del stdout) para asegurar que todas producen el mismo valor.

Todo queda en results.csv y luego plot.py saca las PNG.

📈 ¿Qué se espera ver?

Iterativo (C y Python) debe tener tiempos bajitos y crecer suave con n; memoria estable.

Recursivo (C y Python) sube feo con n (explosión de llamadas).

C le gana a Python porque ejecuta nativo, con menos over­head y tipos estáticos; Python carga VM, GC, objetos dinámicos, etc.

Si no ves diferencia, sube un poquito n (pero con cariño). En py/bench.py ajustas la lista NS.

📊 Ejemplo de tabla 

No pongo números fijos porque cambian por máquina. La idea es el formato y la interpretación.

Lenguaje	Implementación	n	Tiempo (s)	Mem pico (KB)	Resultado
C	Iterativo	30	0.0008	23,4xx	832040
C	Recursivo	30	0.0021	24,1xx	832040
Python	Iterativo	30	0.0040	28,7xx	832040
Python	Recursivo	30	0.1200	35,9xx	832040

Lectura rápida:

Iterativo ≫ Recursivo (gana en tiempo y memoria).

C ≫ Python (por pipeline de ejecución).

Todas calculan el mismo valor, así que no estamos comparando peras con manzanas.

📚 Mini teoría (lo justo para sustentarlo)

Compilado (C): traduce a código máquina antes de correr; con -O2 aplica optimizaciones. Menos sobrecarga en tiempo de ejecución.

Interpretado (Python): ejecuta bytecode sobre una VM con recolección de basura y tipos dinámicos (flexible, pero con costo).

Fibonacci recursivo naive: reconstruye subproblemas una y otra vez → exponencial.

Fibonacci iterativo: pasa de a dos variables (a, b) → O(n) y O(1) memoria.

🧪 Valores por defecto y cómo cambiarlos

En py/bench.py:

NS = [10, 20, 28, 32, 34, 36, 38]


Si vas volado de tiempo: baja la lista (quita 36 y 38).

Si tu PC es un animal y te sobra tiempo: súbele un poquito (pero no mates la recursiva).

🧯 Troubleshooting (cosas que pueden pasar)

cl no existe → abre VS Code desde “x64 Native Tools Command Prompt for VS 2022” o instala los Build Tools.

gcc no existe → instala MinGW-w64 y agrega bin al PATH.

No instala psutil/matplotlib → verifica que abajo a la derecha estás en el entorno correcto (ícono de Python).

Gráficas no salen → revisa que se generó results.csv y mira los logs al correr Python: Bench (VS Code lo muestra todo).

Python recursivo muere por recursión → en py/fib_rec.py ya subí el sys.setrecursionlimit. Si te pasas, igual truena; bájale a n.

🧩 Cómo validarme que todo sí calcula bien

Corre a mano (terminal integrada, no hay problema):

Python

python py/fib_iter.py 30
python py/fib_rec.py 30


C (después de compilar con la tarea de VS Code)

c\bin\fib_iter.exe 30
c\bin\fib_rec.exe 30


Las cuatro deben imprimir 832040 (F(30)).

