# Declaración de variables
nombre = "Nodo1"
cantidad = 10
valorDolar = 7.89
esUltimo = True
valorPuntero = None
semestre = 2
b = 5

# Operaciones aritméticas
suma = cantidad + b
resta = cantidad - b
multiplicacion = cantidad * b
division = cantidad / b
modulo = cantidad % b

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)
print("El módulo es:", modulo)


# Obtener datos del usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))

# Imprimir los datos ingresados por el usuario
print("Hola,", nombre)
print("Tienes", edad, "años")
print("Tu altura es", altura, "metros")


# Ejemplo de operadores lógicos
x = 10
y = 5

# AND: Verdadero si ambas condiciones son verdaderas
resultado_and = x > y and x < 20

# OR: Verdadero si al menos una de las condiciones es verdadera
resultado_or = x > y or y > 100

# NOT: Invierte el valor lógico de la condición
resultado_not = not(x == y)

print("Resultado AND:", resultado_and)
print("Resultado OR:", resultado_or)
print("Resultado NOT:", resultado_not)
