Erweitertes Glossar (einfach & kurz)

(Alphabetisch, damit du schnell nachschlagen kannst.)

Absolute Pfad: vollständiger Dateipfad ab Wurzel (z. B. C:\User\…\beispiel.csv).

API: „Schnittstelle“ zwischen Programmen – Regeln, wie Software miteinander spricht.

Argument: Wert, den du einer Funktion übergibst (z. B. open("datei.txt") → "datei.txt" ist ein Argument).

Array/Liste: geordnete Sammlung von Werten (in Python: list).

ASCII/UTF-8 (Encoding): Art, wie Text intern als Bytes gespeichert wird. UTF-8 ist der Standard, der Umlaute kann.

Ausreißer: sehr ungewöhnlicher Zahlenwert (z. B. 9.999 € unter lauter 10–100 €).

Boolean: Wahrheitswert: True oder False.

Bug: Fehler im Programm oder in Daten.

Bug-Report: strukturierte Beschreibung eines Bugs (Schritte, Erwartung, Ist, Fix).

CLI-Parameter: Start-Optionen für Programme über die Kommandozeile (z. B. python3 main.py --file data.csv).

Column/Spalte: vertikale Datenreihe in einer Tabelle/CSV (z. B. betrag).

CSV: „Comma Separated Values“ – einfache Text-Tabelle, Spalten durch Komma getrennt.

Defaultdict: Wörterbuch (dict), das für neue Schlüssel automatisch einen Startwert hat (hier: 0.0).

Dictionary (dict): Zuordnung Schlüssel → Wert (z. B. {"Köln": 149.40}).

Entry Point: Startdatei eines Projekts (hier: main.py).

Exception: Fehler, der beim Ausführen auftritt (z. B. FileNotFoundError).

float: Gleitkommazahl (z. B. 24.50).

Folder/Verzeichnis: Ordner im Dateisystem.

Funktion: wiederverwendbarer Code-Block (definiert mit def …), z. B. def save_report(...):.

Gherkin: Sprache für Testfälle: Given / When / Then.

Git: Versionskontrolle – speichert Änderungen an Dateien (später nützlich).

ID: eindeutige Kennung (z. B. Kundennummer 1001).

IQR/z-Score: einfache Ausreißer-Heuristiken (Statistik) – brauchst du später.

JSON: Textformat für strukturierte Daten ({"stadt":"Köln","umsatz":149.4}).

Kanal: hier Vertriebskanal (z. B. online, filiale).

Konsolen-Ausgabe: Text, den dein Programm rechts in Replit anzeigt (print(...)).

KPI: Key Performance Indicator – wichtige Kennzahl (z. B. Gesamtumsatz).

Lambda: kurze, anonyme Funktion (hier nur genutzt als Sortier-„Schlüssel“).

Library/Bibliothek: fertige Zusatzfunktionen (in Python per import).

List Comprehension: Kurzschreibweise, um Listen zu bauen (z. B. [x for x in xs if ...]).

Local/Relativer Pfad: Pfad relativ zur aktuellen Datei ("csvprojekt/beispiel.csv").

Logging: systematisches Mitschreiben von Infos/Fehlern in Dateien.

Markdown (.md): leicht lesbares Textformat für Dokus (z. B. README.md).

main(): Hauptfunktion – sammelt die einzelnen Schritte und führt sie aus.

„Main-Guard“: if __name__ == "__main__": → sorgt dafür, dass main() nur startet, wenn die Datei direkt ausgeführt wird (nicht beim Import).

Map/Reduce (grob): Daten transformieren (Map) und zusammenfassen (Reduce/Summen).

Module: einzelne Python-Dateien oder Pakete, die Funktionen/Variablen bereitstellen.

Nullwerte/fehlende Werte: leere Felder in Daten (müssen oft speziell behandelt werden).

Out-of-Range: Wert liegt außerhalb eines sinnvollen Bereichs (z. B. negative Umsätze).

Parsing: Text in echte Datentypen umwandeln (z. B. "24,50" → 24.50).

Path/Pathlib: Python-Werkzeug für Dateipfade (sicherer als reine Strings).

Print: Text in die Konsole schreiben.

Process/Workflow: feste Schritt-Reihenfolge, z. B. Einlesen → Prüfen → Berichten.

Projektstruktur: geordnete Ordner/Dateien (macht Projekte verständlich).

Prototyp: erste einfache Version, die schon läuft.

QA (Quality Assurance): Qualitätssicherung – prüft, ob etwas korrekt ist.

Readme: Start-Dokument, erklärt kurz Zweck, Start, Dateien.

Replit: Online-Entwicklungsumgebung (IDE) im Browser.

Report: Bericht als Datei (hier report.txt).

Return: Ergebnis, das eine Funktion zurückgibt.

Run Command: Befehl, den Replit ausführt, wenn du „Run“ klickst (python3 main.py).

Schema: Spaltenplan einer Tabelle/CSV (Namen/Reihenfolge/Typen).

Shell/Terminal: Text-Konsole für Befehle (z. B. python3 main.py).

Sortieren (mit key=…): Reihenfolge festlegen; key=lambda x: x[1] sortiert nach dem 2. Element eines Paars.

String: Textwert (z. B. "Köln").

Testfall: strukturierte Probe: Given (Ausgangslage), When (Aktion), Then (Erwartung).

try/except: Fehler abfangen; im except entscheidest du, wie du reagierst (z. B. betrag=None).

Variable: benannter Speicherplatz für einen Wert (z. B. umsatz = 181.39).

Versionskontrolle: Änderungen verfolgen/absichern (z. B. Git).

Whitespace/Einrückung: Leerzeichen/Tab – in Python wichtig, um Blöcke zu markieren.

Wörterbuch (dict): siehe Dictionary.

Zahlentypen: int (Ganzzahl), float (Kommazahl).


CSV-Export: Daten als Texttabelle speichern (leicht weiterzugeben).

Header: oberste Zeile mit Spaltennamen.

DictWriter: CSV-Schreibwerkzeug, das mit Python-Wörterbüchern (dict) arbeitet.

parent: der Ordner, in dem eine Datei liegt (txt_path.parent = Ordner von report.txt).