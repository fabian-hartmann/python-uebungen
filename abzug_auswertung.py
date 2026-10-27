# Übungsskript: Prüfung der Einströmgeschwindigkeit an einem Laborabzug gegen einen Grenzwert

print("Auswertung Start")

while True:
    grenzwert = input("Grenzwert in m/s eingeben:").replace(",",".")
    try:
        grenzwert = float(grenzwert)
    except ValueError:
        print("Das ist keine Zahl")
        print("Kein korrekter Grenzwert")
    else:
        if grenzwert > 0:
            break
        else:
            print("Grenzwert muss größer als 0 sein")

messwerte = []
anzahl_zu_niedrig = 0

while True:
    wert = input("Messwerte in m/s eingeben:").replace(",", ".")
    if wert == "":
        break
    else:
        try:
            wert = float(wert)
        except ValueError:
            print("Das ist keine Zahl")
            print("Korrekten Wert eingeben")
        else:
            if wert >= 0:
                messwerte.append(wert)
            else:
                print("Keine negativen Werte")

if len(messwerte) == 0:
    print("Keine Auswertung möglich")
else:
    print("Erfasste Messwerte:", messwerte)
    for wert in messwerte:
        if wert < grenzwert:
            print(wert,"m/s zu niedrig")
            anzahl_zu_niedrig = anzahl_zu_niedrig + 1
        else:
            print(wert,"m/s OK")
    if anzahl_zu_niedrig == 0:
        print("Abzug sicher")
    else:
        print("Anzahl unsichere Messpunkte:", anzahl_zu_niedrig)
        print("Abzug unsicher")
print("Auswertung Ende")