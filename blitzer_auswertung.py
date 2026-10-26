print("Auswertung Start")
messwerte = []  # in km/h
a = 0   #"Klasse 1"
b = 0   #"Klasse 2"
c = 0   #"Klasse 3"

while True:
    grenzwert = input('Grenzwert eingeben:').replace(",", ".")
    try:
       grenzwert=float(grenzwert)
    except ValueError:
        print("keine Zahl")
        print("Korrekten Wert eingeben")
    else:
        if grenzwert <= 0:
            print("Grenzwert muss größer 0 sein")
        else:
            print("Festgelegter Grenzwert:",grenzwert)
            break

while True:
    wert = input("messwerte eingeben:").replace(",", ".")
    if wert == "":
        break
    else:
        try:
            wert = float(wert)
        except ValueError:
            print("keine Zahl")
            print("Korrekten Wert eingeben")
        else:
            if  wert >= 0:
                messwerte.append(wert)
            else:
                print("keine negativen Werte")

print("Messwerte: ",messwerte)

for wert in messwerte:
    if wert >= grenzwert + 10: #Klasse 3
        print("Klasse 3: ",wert)
        c = c + 1
    elif wert >= grenzwert + 5:  #Klasse 2
        print("Klasse 2: ",wert)
        b = b + 1
    elif wert > grenzwert: #Klasse 1
        print("Klasse 1: ",wert)
        a = a + 1
    else:
        print(wert," - OK")

if len(messwerte)==0:
    print("keine Auswertung möglich")
else:
    print("Alle Messwerte Ausgewertet")
    if a > 0 or b > 0 or c > 0:
        r = a + b + c  # Gesamtüberschreitungen
        print("Klasse 1: ",a)
        print("Klasse 2: ",b)
        print("Klasse 3: ",c)
        print("Gesamtüberschreitungen: ",r)
    else:
        print("keine Geschwindigkeitsüberschreitung erfasst")

print("Auswertung beendet")