def calcular_puntos(Kills, assists, deaths):
    """calcula los puntos de un jugador en una ronda"""
    return (Kills*3) + (assists*1) - (1 if  deaths else 0)