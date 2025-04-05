def contar_mensiones(descriptions, palabras_claves):
    #Cuenta las menciones de cada palabra clave en las descripciones.
    #descriptions (list): Lista de descripciones de los streams.
    #palabras_claves (list): Lista de palabras clave a buscar.
    contador = {palabra: 0 for palabra in palabras_claves}
    for description in descriptions:  # Recorremos cada descripción
        for palabra in palabras_claves:  # Recorremos cada palabra clave
            if palabra in description.lower():  # Convertimos la descripción a minúsculas y verificamos si contiene la palabra clave
                contador[palabra] += 1  # Si la palabra clave está presente, aumentamos el contador en 1
    return contador #devolvemos el diccionario con los contadores en cada palabra clave