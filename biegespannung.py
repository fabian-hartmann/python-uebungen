#Berechnung Biegespannung
import math
def wm_rechteck(breite, hoehe):
    widersandsmoment_rechteck = breite * hoehe**2/6
    return widersandsmoment_rechteck
def wm_kreis(durchmesser):
    widerstandsmoment_kreis = math.pi * durchmesser**3/32
    return  widerstandsmoment_kreis
def biegespannung(biegemoment, widerstandsmoment):
    sigma = biegemoment/widerstandsmoment
    return sigma

biegemoment = float(input("Biegemoment in Nm:"))*10**3
sigma_zul = 160

profile = {"Flach_20x40": wm_rechteck(20, 40),"Flach_40x20": wm_rechteck(40,20),"Rund_d30": wm_kreis(30)}

for name, widerstandsmoment in profile.items():
    sigma = biegespannung(biegemoment, widerstandsmoment)
    if sigma > sigma_zul:
        print(name, round(sigma,2),"N/mm²","- Zu hohe Spannung")
    else:
        print(name, round(sigma,2),"N/mm²", "- OK")