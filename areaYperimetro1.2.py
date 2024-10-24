import math

def calcular_area_y_perimetro():
    print("Seleccione una figura geométrica:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Triángulo")

    opcion = input("Ingrese el número de la figura que desea calcular: ")

    if opcion == '1':  # Círculo
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio
        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")

    elif opcion == '2':  # Cuadrado
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        perimetro = 4 * lado
        print(f"El área del cuadrado es: {area:.2f}")
        print(f"El perímetro del cuadrado es: {perimetro:.2f}")

    elif opcion == '3':  # Triángulo
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        lado1 = float(input("Ingrese el lado 1 del triángulo: "))
        lado2 = float(input("Ingrese el lado 2 del triángulo: "))
        lado3 = float(input("Ingrese el lado 3 del triángulo: "))
        
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3
        print(f"El área del triángulo es: {area:.2f}")
        print(f"El perímetro del triángulo es: {perimetro:.2f}")

    else:
        print("Opción no válida. Por favor, seleccione una opción correcta.")

# Ejecutar la función
calcular_area_y_perimetro()
