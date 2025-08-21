# Genera pngs de tiempo y memoria a partir de results.csv
import csv
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise SystemExit("Instala 'matplotlib'.")

ROOT = Path(__file__).resolve().parents[1]
FIGS = ROOT / "figs"

def load_rows():
    rows = []
    with open(ROOT/"results.csv", newline="") as fh:
        for r in csv.DictReader(fh):
            r["n"] = int(r["n"])
            r["time_sec"] = float(r["time_sec"])
            r["mem_kb"] = int(float(r["mem_kb"]))
            rows.append(r)
    return rows

def linea(rows, key):
    xs = [r["n"] for r in rows if (r["lang"], r["impl"]) == key]
    ts = [r["time_sec"] for r in rows if (r["lang"], r["impl"]) == key]
    ms = [r["mem_kb"]   for r in rows if (r["lang"], r["impl"]) == key]
    return xs, ts, ms

def main():
    rows = load_rows()
    FIGS.mkdir(exist_ok=True)

    # Tiempo
    import matplotlib.pyplot as plt
    plt.figure()
    for k in [("C","recursivo"),("C","iterativo"),("Python","recursivo"),("Python","iterativo")]:
        xs, ts, _ = linea(rows, k)
        plt.plot(xs, ts, marker="o", label=f"{k[0]}-{k[1]}")
    plt.xlabel("n"); plt.ylabel("tiempo (s)")
    plt.title("Tiempo: compilado vs interpretado · recursivo vs iterativo")
    plt.grid(True); plt.legend()
    plt.savefig(FIGS/"time_vs_n.png", dpi=160)

    # Memoria
    plt.figure()
    for k in [("C","recursivo"),("C","iterativo"),("Python","recursivo"),("Python","iterativo")]:
        xs, _, ms = linea(rows, k)
        plt.plot(xs, ms, marker="o", label=f"{k[0]}-{k[1]}")
    plt.xlabel("n"); plt.ylabel("memoria pico (KB)")
    plt.title("Memoria: compilado vs interpretado · recursivo vs iterativo")
    plt.grid(True); plt.legend()
    plt.savefig(FIGS/"mem_vs_n.png", dpi=160)

    print("Generado: figs/time_vs_n.png, figs/mem_vs_n.png")

if __name__ == "__main__":
    main()
