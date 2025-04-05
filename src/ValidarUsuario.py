def contiene_numero(usuario):
    # Verificar que el nombre de usuario tenga al menos un número
    for char in usuario:
        if char.isdigit():  # Si el carácter es un número
            return True
    return False # si no encuentro numero

def contiene_mayuscula(usuario):
    #verifica que tenga al menos una mayuscula 
    for char in usuario:
        if char.isupper():
            return True
    return False

def contiene_letras_y_numeros(usuario):
    for char in usuario:
        if not (("A" <= char <= "Z") or ("a" <= char <= "z") or char.isdigit()):
            return False # si no es letra o numero 
    return True # si solo tiene letras y numeros 

def validar_usuario(usuario):
    #verificar que el nombre de usuario tenga al menos 5 caracteres 
    if len(usuario) < 5:
        return "El nombre de usuario no cumple con los requisitos"

    #verificar si al menos tiene un numero 
    if not contiene_numero(usuario):
        return "El nombre de usuario no cumple con los requisitos"
    
    #verificar si al menos tiene una letra mayuscula 
    if not contiene_mayuscula(usuario):
        return "El nombre de usuario no cumple con los requisitos"

    #verificar que solo pueda contener letras y numeros 
    if not contiene_letras_y_numeros(usuario):
        return "El nombre de usuario no cumple con los requisitos"

    # si paso las validaciones es valido 
    return "Nombre de usuario valido"