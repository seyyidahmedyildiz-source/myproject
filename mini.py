import csv

def parse_betrag(text):
  s = (text or "" ).strip()
  if not s:
      return None

  if "," in s:
    s = s.replace(".", "")
    s = s.replace(",", ".")
  return float(s)
    
rows = []

with open("beispiel.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        r["betrag"] = parse_betrag(r["betrag"])
        rows.append(r)
        
umsatz_pos = sum(r["betrag"] for r in rows if (r["betrag"] or 0) >= 0)
print(f"Umsatz >= 0: {umsatz_pos:.2f}")