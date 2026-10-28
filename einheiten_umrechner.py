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
kmh = 80
print(f"Geschwindigkeit umgerechnet: {kmh} km/h = {kmh_zu_ms(kmh):.2f} m/s")

# Umrechnung bar in pa
bar = 3
print(f"Druck umgerechnet: {bar} bar = {bar_zu_pa(bar):.0f} Pa")

# Umrechnung °C in K
temp_c = 30
print(f"Temperatur umgerechnet: {temp_c} °C = {celsius_zu_kelvin(temp_c):.2f} K")

print("Umrechnungen Ende")