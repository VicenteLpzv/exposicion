import random  # Importamos la librería random para generar números aleatorios

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0  # Inicializamos los intentos en 0

print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinarlo?")

# Bucle que sigue hasta que el jugador adivine el número
while True:
    intento = input("Introduce tu número: ")

    try:
        #  convertir la entrada a un número entero
        intento = int(intento)

        # Verificamos que el número no sea negativo
        if intento < 0:
            print("Por favor, ingresa un número positivo.")
            continue  # Volvemos al inicio del bucle para pedir otro intento

        intentos += 1  # Incrementamos los intentos

        # Comparamos el número ingresado con el número secreto
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break  # Salimos del bucle si el jugador adivina el número

    except ValueError:
        print("Por favor, ingresa un número válido.")

