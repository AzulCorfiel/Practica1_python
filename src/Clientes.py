def limpiar_clientes(clientes):
    """
    Esta función toma una lista de nombres de clientes y devuelve una lista limpia
    con los nombres únicos, eliminando duplicados y espacios innecesarios.
    """
    
    #Eliminar valores nulos y vacíos
    clientes_limpios = [cliente.strip() for cliente in clientes if cliente and cliente.strip()]

    #Convertir a formato título manualmente 
    def formato_titulo(nombre):
        palabras = nombre.lower().split()  # Convertir a minúsculas y dividir por espacios
        resultado = []
        for palabra in palabras:
            if len(palabra) > 0:
                resultado.append(palabra[0].upper() + palabra[1:])  # Primera letra en mayúscula manualmente
            else:
                resultado.append("")
        return " ".join(resultado)
    
    clientes_limpios = [formato_titulo(cliente) for cliente in clientes_limpios]
    #Eliminar duplicados
    clientes_unicos = [] #lista para guardar sin duplicados
    vistos = set() #conjunto set para guardar los nombres vistos
    for cliente in clientes_limpios:
        if cliente not in vistos: #verifico si el cliente ya se agrego
            clientes_unicos.append(cliente) #lo agrego a la lista de clientes unicos
            vistos.add(cliente) #lo agrego para que la proxima iteracion no lo agregue
    
    clientes_limpios = sorted(clientes_unicos)  # Ordenar la lista final alfabéticamente
    
    return clientes_limpios