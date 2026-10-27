# Übungsskript: Auswertung gemessener Geschwindigkeiten gegen eine Höchstgeschwindigkeit mit Einteilung in Überschreitungsklassen

print("Auswertung Start")
messwerte = []  # in km/h
klasse_1 = 0
klasse_2 = 0
klasse_3 = 0

while True:
    grenzwert = input("Grenzwert in km/h eingeben:").replace(",", ".")
    try:
        grenzwert = float(grenzwert)
    except ValueError:
        print("Keine Zahl")
        print("Korrekten Wert eingeben")
    else:
        if grenzwert <= 0:
            print("Grenzwert muss größer 0 sein")
        else:
            print("Festgelegter Grenzwert:", grenzwert)
            break

while True:
    wert = input("Messwerte in km/h eingeben:").replace(",", ".")
    if wert == "":
        break
    else:
        try:
            wert = float(wert)
        except ValueError:
            print("Keine Zahl")
            print("Korrekten Wert eingeben")
        else:
            if wert >= 0:
                messwerte.append(wert)
            else:
                print("Keine negativen Werte")

if len(messwerte) == 0:
    print("Keine Auswertung möglich")
else:
    print("Messwerte: ", messwerte)
    for wert in messwerte:
        if wert >= grenzwert + 10:
            print("Klasse 3: ", wert, "km/h")
            klasse_3 = klasse_3 + 1
        elif wert >= grenzwert + 5:
            print("Klasse 2: ", wert, "km/h")
            klasse_2 = klasse_2 + 1
        elif wert > grenzwert:
            print("Klasse 1: ", wert, "km/h")
            klasse_1 = klasse_1 + 1
        else:
            print(wert, "km/h", " - OK")

    gesamt_ueberschreitungen = klasse_1 + klasse_2 + klasse_3
    if gesamt_ueberschreitungen > 0:
        print("Klasse 1 - bis unter 5 km/h zu schnell: ", klasse_1)
        print("Klasse 2 - 5 bis unter 10 km/h zu schnell: ", klasse_2)
        print("Klasse 3 - ab 10 km/h zu schnell: ", klasse_3)
        print("Gesamtüberschreitungen: ", gesamt_ueberschreitungen)
    else:
        print("Keine Geschwindigkeitsüberschreitung erfasst")

print("Auswertung beendet")