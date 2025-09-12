# CSV-Audit (Mini-Projekt)

**Ziel (kurz):** Eine kleine Datendatei im CSV-Format (Comma Separated Values = Texttabelle) wird geprüft (**Datenqualität**) und zusammengefasst (**KPIs = Kernzahlen**).  
**Warum relevant:** So arbeiten Data-Quality/QA/Support-Rollen in IT/AI-Teams: Dateien einlesen → prüfen → Bericht.

---

## Daten
Beispiel: `beispiel.csv`


**Spalten (Schema = Spaltenplan):** `kunde, stadt, betrag, kanal`  
**Konvention:** `betrag` ist Zahl (Dezimaltrennzeichen akzeptiert: „,“ oder „.“).

---

## Was das Skript macht
1. **Einlesen & Parsen** (Text → Zahl; „24,50“ wird zu `24.50`).  
2. **Qualitätschecks:** fehlende Werte, `betrag ≤ 0`.  
3. **Bereinigte Sicht:** nur `betrag > 0`.  
4. **KPIs:** Gesamtumsatz, Anzahl positiver Transaktionen, Durchschnittsbon, Umsatz je Stadt/Kanal.  
5. **Bericht ausgeben** (Konsole) **und** in `report.txt` speichern.

---

## So startest du es (Replit)
- Datei `main.py` öffnen → **Run** (Run command: `python3 main.py`).  
- Alternativ in der **Shell (Terminal)**: `python3 main.py`

**Erwartete Ausgabe (Sollwerte):**
- Gesamtumsatz **181.39 €**, positive Transaktionen **5**, Durchschnittsbon **36.28 €**  
- Stadt: Köln **149.40 €**, Bonn **31.99 €**  
- Kanal: filiale **97.00 €**, online **84.39 €**

---

## QA (Qualitätssicherung – kurz)
- **Testfall 1 (Komma-Dezimal):** `"24,50"` wird korrekt als `24.50` verarbeitet.  
- **Testfall 2 (≤0-Beträge):** `0.00`/`-5.00` gehen nicht in die KPIs, sondern in die Fehlergruppe.  
- **Bug-Fix:** Dezimal-Komma wird vor `float()` zu Punkt ersetzt.

---

## Dateien
- `main.py` – Hauptprogramm (Entry Point = Startdatei)  
- `beispiel.csv` – Eingabedaten  
- `report.txt` – Textbericht

---

## Nächste Schritte (optional)
- **Unit-Tests** (automatische Mini-Tests) hinzufügen.  
- **CLI-Parameter** (Start-Optionen, z. B. `--file pfad.csv`).  
- **JSON-Report** für Weiterverarbeitung.

„Benutzung (CLI)“ mit den Befehlen oben.
„Maschinenlesbarer Output (JSON)“ – kurzer JSON-Ausschnitt.
„Selbsttest“ – ein Satz: „Beim Start laufen 2 Assertions (Komma-Dezimal, ≤0-Filter).“

python3 main.py                             # Standard
python3 main.py --in meine.csv --txt out.txt --json out.json

Exports

report.txt (Textbericht)

report.json (maschinenlesbar/JSON)

stadt_umsatz.csv (Spalten: stadt, umsatz, anteil_prozent)

fehler.csv (Spalten: kunde, stadt, betrag, kanal, grund)

3 Mini-Insights

Köln ≈ 82.4 % Umsatzanteil (dominant).

Filiale > Online (53.5 % vs. 46.5 %).

1 Zeile mit 0,00 € korrekt ausgeschlossen → Qualitätslogik greift.

(Begriffe: JSON = strukturiertes Textformat, CSV = Texttabelle, Assertion = Auto-Check, CLI = Startoptionen.)