# Bug Report: Komma-Dezimaltrenner ohne Vorverarbeitung

**Umgebung:** Replit (Python 3.11), Standardbibliothek `csv`, Projekt "CSV-Audit"  
**Beschreibung:** Werte wie `"24,50"` in der Spalte `betrag` verursachen ohne Ersetzung eine Exception.

## Schritte zur Reproduktion
1. CSV mit `betrag = "24,50"` laden.
2. Ohne Ersetzung `,` → `.` versuchen, per `float("24,50")` zu parsen.
3. Programm bricht mit `ValueError` ab.

## Erwartetes Verhalten
- Dezimal-Komma wird akzeptiert (durch Vorverarbeitung `replace(",", ".")`), **oder**
- Zeile wird als Fehler markiert; restliche Verarbeitung läuft weiter.

## Tatsächliches Verhalten
- `ValueError`, Verarbeitung stoppt (ohne Vorverarbeitung).

## Fix (implementiert)
- Vor `float()`: `str(betrag).replace(",", ".")`

## Schweregrad / Priorität
- Mittel / Hoch (blockiert KPI-Erstellung ohne Workaround)
