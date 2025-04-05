def son_anagramas(palabra1, palabra2):
    # Convertimos las palabras a minúsculas y eliminamos espacios
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    
    # Comparamos las letras de ambas palabras
    return sorted(palabra1) == sorted(palabra2)