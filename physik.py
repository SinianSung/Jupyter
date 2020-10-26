import numpy as np

m = 1.
k = 1.
g = 9.81


# Berechnung der Bewegung
def f(v, t0, k, typus="none"):
    """
    turbulente Luftströmung
    typus = "newton" oder "stokes"
    """
    # v hat vier komponenten: v = [x,y,v_x,v_y]
    u, udot = v[:2], v[2:]
    # Berechnung der Beschleunigung
    if typus=="newton":
        udotdot = -k / m * udot *udot
    elif typus=="stokes":
        udotdot = -k / m * udot
    else:
        if (udot[0]**2 + udot[1]**2 >80):
            udotdot = -k / m * udot *udot
        else:
            udotdot = -k / m * udot
    udotdot[1] -= g
    # Rückgabe neuer v-Wert  v'=[u', u''].
    if u[1]>=0:
        return np.r_[udot, udotdot]
    else:
        # abschneiden falls die Werte unter 0 sind (nummerische Probleme vermeiden)
        return np.r_[udot, [0,0]]