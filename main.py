import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
import argparse  # neu
import json  # für Block B
import csv
from collections import defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).parent.resolve()
CSV_PATH = Path("beispiel.csv")
REPORT_PATH = Path("report.txt")

def read_rows(csv_path: Path):
    if not csv_path.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {csv_path.resolve()}")
    rows = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            val = str(r.get("betrag", "")).replace(",", ".")
            try:
                r["betrag"] = float(val)
            except Exception:
                r["betrag"] = None
            rows.append(r)
    return rows


def audit(rows):
    fehler = [
        r for r in rows
        if (r["betrag"] is None) or (r.get("kunde") in (None, ""))
    ]
    neg0 = [
        r for r in rows if isinstance(r["betrag"], float) and r["betrag"] <= 0
    ]
    pos = [
        r for r in rows if isinstance(r["betrag"], float) and r["betrag"] > 0
    ]

    umsatz = sum(r["betrag"] for r in pos)
    anzahl = len(pos)
    durchschnitt = (umsatz / anzahl) if anzahl else 0.0

    by_stadt = defaultdict(float)
    by_kanal = defaultdict(float)
    for r in pos:
        by_stadt[r["stadt"]] += r["betrag"]
        by_kanal[r["kanal"]] += r["betrag"]

    return {
        "fehler_count": len(fehler),
        "neg0_count": len(neg0),
        "pos_count": len(pos),
        "umsatz": umsatz,
        "durchschnitt": durchschnitt,
        "by_stadt": dict(by_stadt),
        "by_kanal": dict(by_kanal),
    }


def save_report(result, path: Path = REPORT_PATH):
    # Report schreiben
    with path.open("w", encoding="utf-8") as out:
        out.write("=== Qualitätsbericht ===\n")
        out.write(
            f"Fehlerhafte Zeilen: {result['fehler_count']}  |  <=0 EUR: {result['neg0_count']}  |  Positive: {result['pos_count']}\n\n"
        )
        out.write("=== KPIs ===\n")
        out.write(
            f"Gesamtumsatz: {result['umsatz']:.2f} EUR   |   Durchschnittsbon: {result['durchschnitt']:.2f} EUR\n\n"
        )
        out.write("Umsatz je Stadt:\n")
        for k, v in sorted(result["by_stadt"].items(),
                           key=lambda x: x[1],
                           reverse=True):
            out.write(f"  - {k}: {v:.2f} EUR\n")
        out.write("\nUmsatz je Kanal:\n")
        for k, v in sorted(result["by_kanal"].items(),
                           key=lambda x: x[1],
                           reverse=True):
            out.write(f"  - {k}: {v:.2f} EUR\n")

    print(f"\n[OK] Report gespeichert als: {path.resolve()}")


def parse_args():
    p = argparse.ArgumentParser(description="CSV-Audit v2")
    p.add_argument("--in",
                   dest="infile",
                   default="beispiel.csv",
                   help="Eingabedatei (CSV)")
    p.add_argument("--txt",
                   dest="txt_out",
                   default="report.txt",
                   help="Ausgabe Textbericht")
    p.add_argument("--json",
                   dest="json_out",
                   default="report.json",
                   help="Ausgabe JSON-Report")
    return p.parse_args()


def self_test(audit_fn):
    # 1) Komma-Dezimal muss funktionieren
    rows = [
        {
            "kunde": "1",
            "stadt": "Köln",
            "betrag": "24,50",
            "kanal": "online"
        },
        {
            "kunde": "2",
            "stadt": "Bonn",
            "betrag": "0.00",
            "kanal": "filiale"
        },
    ]
    # Parsing wie im echten Code
    for r in rows:
        val = str(r.get("betrag", "")).replace(",", ".")
        try:
            r["betrag"] = float(val)
        except:
            r["betrag"] = None

    res = audit_fn(rows)
    assert res["pos_count"] == 1, "Erwarte 1 positive Transaktion"
    assert round(res["umsatz"], 2) == 24.50, "Erwarte Umsatz 24.50"
    print("[Test] OK: Komma-Dezimal & ≤0-Filter")


# -- Export: Stadt-Zusammenfassung als CSV --
def write_city_summary_csv(result: dict, out_path):
    # result["by_stadt"] = {"Köln": 149.4, "Bonn": 31.99, ...}
    total = result["umsatz"] or 1.0
    rows = []
    for stadt, umsatz in sorted(result["by_stadt"].items(),
                                key=lambda x: x[1],
                                reverse=True):
        anteil = round(100.0 * umsatz / total, 1)
        rows.append({
            "stadt": stadt,
            "umsatz": round(umsatz, 2),
            "anteil_prozent": anteil
        })
    # CSV schreiben
    import csv
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["stadt", "umsatz", "anteil_prozent"])
        w.writeheader()
        w.writerows(rows)


# -- Export: Fehlerliste als CSV --
def write_error_list_csv(all_rows: list, out_path):
    """
    Schreibt alle problematischen Zeilen:
      - betrag ist None (nicht parsebar) ODER
      - betrag <= 0 ODER
      - kunde fehlt/leer
    mit einer Spalte 'grund' (warum die Zeile fehlerhaft ist).
    """
    bad = []
    for r in all_rows:
        grund = None
        if r.get("kunde") in (None, ""):
            grund = "kunde fehlt/leer"
        # betrag kann None sein oder Zahl <= 0
        b = r.get("betrag")
        if b is None:
            grund = (grund +
                     "; betrag ungueltig") if grund else "betrag ungueltig"
        elif isinstance(b, (int, float)) and b <= 0:
            grund = (grund + "; betrag<=0") if grund else "betrag<=0"
        if grund:
            bad.append({
                "kunde": r.get("kunde"),
                "stadt": r.get("stadt"),
                "betrag": r.get("betrag"),
                "kanal": r.get("kanal"),
                "grund": grund
            })
    # CSV schreiben (nur wenn es etwas gibt; sonst leere Datei mit Header)
    import csv
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["kunde", "stadt", "betrag", "kanal", "grund"])
        w.writeheader()
        w.writerows(bad)


def main():
    args = parse_args()
    logging.info("Start CSV-Audit")
    self_test(audit)  # führt die 2 Checks aus; bricht bei Fehlern ab
    from pathlib import Path
    csv_path = Path(args.infile)
    txt_path = Path(args.txt_out)
    json_path = Path(args.json_out)

    rows = read_rows(CSV_PATH)
    logging.info("CSV geladen: %s | Zeilen: %d", csv_path, len(rows))
    result = audit(rows)
    logging.info(
        "KPIs: umsatz=%.2f | pos=%d | durchschnitt=%.2f",
        result["umsatz"], result["pos_count"], result["durchschnitt"]
    )


    total = result["umsatz"] or 1.0
    # Stadt-Prozente
    print("\nAnteile je Stadt (% vom Umsatz):")
    for k, v in sorted(result["by_stadt"].items(),
                       key=lambda x: x[1],
                       reverse=True):
        print(f"  - {k}: {100.0 * v/total:5.1f}%")
    # Kanal-Prozente
    print("\nAnteile je Kanal (% vom Umsatz):")
    for k, v in sorted(result["by_kanal"].items(),
                       key=lambda x: x[1],
                       reverse=True):
        print(f"  - {k}: {100.0 * v/total:5.1f}%")
    # ------ Mini-Projekt 3: CSV-Exporte ------
    # export-Verzeichnis: dort, wo dein Text-/JSON-Report liegen (meist Projekt-Root)
    out_dir = Path(".")
    try:
        # falls du schon Variablen wie txt_path/json_path hast, nimm deren Ordner:
        out_dir = txt_path.parent
    except:
        pass

    stadt_csv = out_dir / "stadt_umsatz.csv"
    fehler_csv = out_dir / "fehler.csv"

    write_city_summary_csv(result, stadt_csv)
    write_error_list_csv(rows, fehler_csv)

    print(f"[OK] Stadt-Zusammenfassung (CSV): {stadt_csv}")
    print(f"[OK] Fehlerliste (CSV):          {fehler_csv}")

    # >>> Report ausgeben
    print("=== Qualitätsbericht ===")
    print(
        f"Fehlerhafte Zeilen: {result['fehler_count']}  |  <=0 EUR: {result['neg0_count']}  |  Positive: {result['pos_count']}"
    )
    print("\n=== KPIs ===")
    print(
        f"Gesamtumsatz: {result['umsatz']:.2f} EUR   |   Durchschnittsbon: {result['durchschnitt']:.2f} EUR"
    )
    print("\nUmsatz je Stadt:")
    for k, v in sorted(result["by_stadt"].items(),
                       key=lambda x: x[1],
                       reverse=True):
        print(f"  - {k}: {v:.2f} EUR")
    print("\nUmsatz je Kanal:")
    for k, v in sorted(result["by_kanal"].items(),
                       key=lambda x: x[1],
                       reverse=True):
        print(f"  - {k}: {v:.2f} EUR")

    summary = {
        "gesamtumsatz": round(result["umsatz"], 2),
        "positive_transaktionen": result["pos_count"],
        "durchschnittsbon": round(result["durchschnitt"], 2),
        "umsatz_je_stadt": result["by_stadt"],
        "umsatz_je_kanal": result["by_kanal"],
    }
    with json_path.open("w", encoding="utf-8") as jf:
        json.dump(summary, jf, ensure_ascii=False, indent=2)

    print(f"\n[OK] Textbericht: {txt_path}")
    print(f"[OK] JSON-Report: {json_path}")

    # >>> Report schreiben
    save_report(result)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.exception("Fehler im Lauf")
        raise
