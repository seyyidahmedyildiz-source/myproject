# Testfälle (Given/When/Then)

## Testfall 1 — Komma-Dezimal
**Given:** CSV-Zeile mit `betrag = "24,50"`  
**When:** `main.py` wird gestartet  
**Then:** `betrag` wird als `24.50` (float) gelesen und zählt zu den **positiven** Transaktionen

## Testfall 2 — Null/Negativ
**Given:** CSV-Zeile mit `betrag = 0.00` (oder `-5.00`)  
**When:** `main.py` wird gestartet  
**Then:** Zeile landet in der **≤0-Gruppe** und **nicht** in den KPIs

## Testfall 3 — Fehlerhafter Wert
**Given:** CSV-Zeile mit `betrag = "abc"`  
**When:** `main.py` wird gestartet  
**Then:** Zeile wird als **fehlerhaft** gezählt (nicht in KPIs), Programm läuft weiter
