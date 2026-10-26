print("Auswertung Start")

while True:
    grenzwert = input("Grenzwert eingeben:").replace(",",".")   # m/s
    try:
        grenzwert = float(grenzwert)
    except ValueError:
        print("Das ist keine Zahl")
        print("Kein Korrekter Grenzwert")
    else:
        if grenzwert > 0:
            break
        else:
            print("Grenzwert muss größer als 0 sein")

messwerte=[]
r=0

while True:
    wert = input("Messwerte eingeben:").replace(",", ".")
    if wert == "":
       break
    else:
        try:
            wert = float(wert)

        except ValueError:
            print("Das ist keine Zahl")
            print("Korrekten wert eingeben")

        else:
            if wert >= 0:
                messwerte.append(wert)
            else:
                print("keine negativen Werte")

if len(messwerte) == 0:
    print("keine Auswertung möglich")
else:
    print(messwerte)

    for wert in messwerte:

        if wert < grenzwert:
            print(wert,"m/s zu niedrig")
            r=r+1
        else:
            print(wert,"m/s OK")

    if r==0:
        print("Abzug sicher")
    else:
        print(r, "Anzahl unsichere Messpunkte")
        print("Abzug unsicher")
print("Auswertung Ende")