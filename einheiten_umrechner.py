# Übung: Umrechnung verschiedener Einheiten


def kmh_zu_ms(kmh):
    ms = kmh/3.6
    return ms


def bar_zu_pa(bar):
    pa = bar*10**5
    return pa


def celsius_zu_kelvin(temp_c):
    temp_k = temp_c + 273.15
    return temp_k


print("Umrechnungen Start")

# Umrechnung km/h in m/s
print("Geschwindigkeit umgerechnet:", "10 km/h =", round(kmh_zu_ms(10), 2), "m/s")

# Umrechnung bar in pa
print("Druck umgerechnet:", "1 bar =", bar_zu_pa(1), "Pa")

# Umrechnung °C in K
print("Temperatur umgerechnet:", "30 °C =", celsius_zu_kelvin(30), "K")

print("Umrechnungen Ende")