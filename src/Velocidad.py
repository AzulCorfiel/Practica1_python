def chequear (respuesta):
    if respuesta < 200:
        return "Rapido"
    elif (200 <= respuesta <= 500):
        return "Normal"
    elif (respuesta > 500):
        return "Lento"