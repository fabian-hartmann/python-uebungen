# Python-Übungen 
Mein Name ist Fabian Hartmann, ich bin Maschinenbauabsolvent und mein Ziel dieser Übungen ist es, die Fähigkeit zu erwerben, eigene Skripte für technische Berechnungen und messtechnische Auswertungen zu erstellen. 
Dieses Projekt läuft seit Oktober 2026. 

## Inhalt 

### abzug_auswertung.py 
Diese Übung dient dazu, Geschwindigkeitsmessungen auszuwerten. 
Das Thema ist an meine Bachelorarbeit angelehnt.

Aufbau Skript:
- Es startet mit der Eingabe des Grenzwerts und der Messwerte. 
- Es enthält Eingabeprüfungen mittels try/except. 
- Zählen der unsicheren Messwerte, falls vorhanden. 
- Es folgt die Ausgabe, ob der Abzug sicher oder unsicher ist.

### blitzer_auswertung.py
Diese Übung dient dazu, Geschwindigkeitsmessungen gegen eine Höchstgeschwindigkeit auszuwerten.

Aufbau Skript:
- Es startet mit der Eingabe des Grenzwerts und der Messwerte. 
- Es enthält Eingabeprüfungen mittels try/except. 
- Die Fälle werden mittels elif unterschieden. 
- Es folgt die Ausgabe, gesamt und in Klassen, falls Überschreitungen vorhanden sind. 

### biegespannung.py 
Diese Übung dient dazu, Funktionen zu definieren und diese abzurufen. 
Zusätzlich soll ein Dictionary sinnvoll eingebunden werden. 
Vergleich von Flachstahl hochkant, Flachstahl liegend und Rundstab bei gleichem Biegemoment. 

Aufbau Skript:
- Es werden die für die Berechnung der Biegespannungen benötigten Formeln definiert. 
- Es werden verschiedene Fallbeispiele im Dictionary gespeichert.
- Es wird ausgewertet, ob die vorab maximal zulässige Biegespannung überschritten wird. 
- Darin wird eine for-Schleife verwendet, die auf das Dictionary zurückgreift und die Funktion für die Biegespannung beinhaltet. 

### einheiten_umrechner.py

Diese Übung dient dazu, Funktionen zu definieren und Einheiten passend umrechnen zu können. 

Aufbau Skript:
- Es werden Funktionen der verschiedenen Umrechnungsfälle definiert. 
- Anschließend werden die Umrechnungen unter Verwendung der Funktionen ausgegeben. 

## Ausführen 

Version: Python 3 (getestet mit 3.14) 

- `python einheiten_umrechner.py` 
- `python blitzer_auswertung.py` 
- `python abzug_auswertung.py` 
- `python biegespannung.py` 

## Geplant 

Folgende Themen sind geplant: Messdaten aus CSV-Dateien einlesen, Diagramme mit Matplotlib und Berechnungen mit NumPy.
Diese werden künftig dem Repository hinzugefügt. 