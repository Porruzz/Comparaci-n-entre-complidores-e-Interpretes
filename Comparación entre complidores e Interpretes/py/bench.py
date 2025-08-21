# Benchmark en Windows: mide TIEMPO y MEMORIA (RSS pico aproximado) de:
#   C-recursivo, C-iterativo, Python-recursivo, Python-iterativo.
# Genera results.csv y llama a plot.py para crear las gráficas.
import time, csv, subprocess
from pathlib import Path

try:
    import psutil
except ImportError:
    raise SystemExit("Instala 'psutil' y 'matplotlib' (requirements.txt).")

ROOT = Path(__file__).resolve().parents[1]
BIN  = ROOT / "c" / "bin"

# Conjunto de tamaños: pensado para correr rápido pero mostrar tendencia
NS = [10, 20, 28, 32, 34, 36, 38]  # ojo: la recursiva se vuelve muy lenta > 40

def run_and_measure(cmd):
    t0 = time.perf_counter()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p = psutil.Process(proc.pid)
    peak_kb = 0
    while True:
        if proc.poll() is not None:
            break
        try:
            rss = p.memory_info().rss // 1024
            if rss > peak_kb: peak_kb = rss
        except psutil.NoSuchProcess:
            break
        time.sleep(0.002)
    out, _ = proc.communicate()
    t1 = time.perf_counter()
    return out.strip(), (t1 - t0), peak_kb

def main():
    rows = []
    tasks = [
        ("C",      "recursivo",  [str(BIN/"fib_rec.exe")]),
        ("C",      "iterativo",  [str(BIN/"fib_iter.exe")]),
        ("Python", "recursivo",  ["python", str(ROOT/"py"/"fib_rec.py")]),
        ("Python", "iterativo",  ["python", str(ROOT/"py"/"fib_iter.py")]),
    ]
    for lang, impl, base in tasks:
        for n in NS:
            out, t, kb = run_and_measure(base + [str(n)])
            res = out.splitlines()[-1] if out else ""
            rows.append({"lang":lang, "impl":impl, "n":n, "time_sec":t, "mem_kb":kb, "result":res})
            print(f"{lang:7} {impl:9} n={n:2d} -> t={t:6.3f}s  mem={kb:7d} KB  res={res}")

    with open(ROOT/"results.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["lang","impl","n","time_sec","mem_kb","result"])
        w.writeheader(); w.writerows(rows)

    # crear gráficas
    subprocess.run(["python", str(ROOT/"py"/"plot.py")], check=True)

if __name__ == "__main__":
    main()
