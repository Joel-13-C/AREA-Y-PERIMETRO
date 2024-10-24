
# Función para calcular el área de un círculo
def area_circulo(radio):
    return 3.1416 * radio**2

# Función para calcular el área de un cuadrado
def area_cuadrado(lado):
    return lado * lado

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# Menú para seleccionar la figura geométrica
def menu():
    print("Selecciona la figura geométrica:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Triángulo")
    opcion = int(input("Ingresa el número de la opción: "))
    return opcion

def main():
    opcion = menu()

    if opcion == 1:
        radio = float(input("Ingresa el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio)}")
    elif opcion == 2:
        lado = float(input("Ingresa el lado del cuadrado: "))
        print(f"El área del cuadrado es: {area_cuadrado(lado)}")
    elif opcion == 3:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")
    elif opcion == 4:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        print(f"El área del triángulo es: {area_triangulo(base, altura)}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
