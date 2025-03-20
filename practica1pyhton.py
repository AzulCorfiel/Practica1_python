import random
import sys
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?","¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas
#unimos las 3 listas en una sola estructura de datos 
question_data = list(zip(questions, answers, correct_answers_index))

#seleccionamos 3 preguntas aleatorias
question_to_ask = random.choice(question_data,	k=3)

puntaje = 0

# Preguntas al usuario
for questions, options, correct_index in question_to_ask:
    print(questions)  # Muestra la pregunta  Itera sobre las opciones y las muestra numeradas
    
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        print()
        user_answer = input("Respuesta: ")  # Entrada del usuario

        # Verificamos que la entrada sea un número
        if not user_answer.isdigit():
            print("Algo salió mal. Terminando el programa.")
            sys.exit(1)
			
        user_answer = int(user_answer) - 1#convierto en base 0 para chequear si esta en 1-4
		 
        if user_answer not in [0, 1, 2, 3]: # verifica que la respuesta sea valida 
            print("Algo salió mal. Terminando el programa.")
            sys.exit(1)

         # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            print("¡Correcto! (+1 punto)")
            puntaje += 1
            print()
            break
        else:   #respuesta incorrecta
            puntaje -= 0.5
            if intento < 1: #aun queda un intento
                print("Incorrecto.	Tienes otra oportunidad.		(-0.5	puntos)")
            else:   #ya no quedan intentos
                print(f"Incorrecto. La respuesta correcta era: {options[correct_index]}")  
    print()
print(f"Puntaje total: {puntaje}")

