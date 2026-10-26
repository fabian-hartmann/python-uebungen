#Umrechnung km/h in m/s
def kmh_zu_ms(kmh):
    ms = kmh/3.6
    return ms

print("Geschwindigkeit umgerechnet:",round(kmh_zu_ms(10), 2),"m/s")

#Umrechnung bar in Pa
def bar_zu_Pa(bar):
    Pa = bar*10**5
    return Pa

print("Druck umgerechnet:",bar_zu_Pa(1),"Pa")

#Umrechnung °C in K

def celsius_zu_kelvin(temp_C):
    temp_K = temp_C + 273.15
    return temp_K

print("Temperatur umgerechnet:",celsius_zu_kelvin(30),"K")
print("Umrechnung beendet")