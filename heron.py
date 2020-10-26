import matplotlib.pyplot as plt
import math

"""
    Berechnung der Wurzel von a mit Hilfe einer
    rekursiven Folge
    a_0 radikand
"""

def __dir__():
    return "help"

def heronschritt(wert, radikand = 10):
    """
    berechnet das nächste Folgenglied
    wert = momentaner schätzwert
    radikand, standardwert ist 10
    """
    wert = 1/2*(wert + radikand/wert)
    return wert

def heronverfahren(startwert,radikand, genauigkeit = 5):
    """
        bestimmt wie viele Schritte nötig sind um die Wurzel von
        radikand auf die vorgegebene Genauigkeit zu bestimmen.
        genauigkeit = 5
    """
    genauigkeit = 10**(-genauigkeit)
    messung = genauigkeit +1
    wert = startwert
    schritte = 0
    while messung > genauigkeit:
        wert = heronschritt(wert,radikand)
        messung = wert - heronschritt(wert,radikand)
        schritte += 1
    print("In {} Schritten hat man den Wert {} erreicht. (Genauigkeit = {})".format(schritte, wert, genauigkeit))