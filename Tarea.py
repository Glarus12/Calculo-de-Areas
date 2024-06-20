import math

#Triangulo

Base_Triangulo = float (input ("¿Cual es la medida de la base del triangulo? "))
Altura_Triangulo = float (input ("¿Cual es la altura del triangulo? "))
Area = Base_Triangulo * Altura_Triangulo / 2
print (f"El área del triangulo es: {Area:.2f}")

#Circulo

Radio_Circulo = float (input ("¿Cual es el radio del circulo? "))
Area_Circulo = math.pi * Radio_Circulo ** 2
print (f"El área del circulo es: {Area_Circulo:.2f}")

#Rectangulo Torso

Largo_Rectangulo = float (input ("¿Cual es el largo del torso? "))
Ancho_Rectangulo = float (input ("¿Cual es la ancho del torso? "))
Area_Torso = Largo_Rectangulo * Ancho_Rectangulo
print (f"El área del torso es: {Area_Torso:.2f}")

#Brazos

Largo_Brazo = float (input ("¿Cual es el largo de un brazo? "))
Ancho_Brazo = float (input ("¿Cual es el ancho de un brazo? "))
Area_Brazo = Largo_Brazo * Ancho_Brazo
print (f"El área del brazo es: {Ancho_Brazo:.2f}")

#Piernas

Largo_Pierna = float (input ("¿Cual es el largo de una pierna? "))
Ancho_Pierna = float (input ("¿Cual es el ancho de una pierna? "))
Area_Pierna = Largo_Pierna * Ancho_Pierna
print (f"El área de la pierna es: {Area_Pierna:.2f}")

#Total

Area_Completa = Area_Circulo + Altura_Triangulo + Ancho_Rectangulo
Area_Brazos = Area_Brazo * 2
Area_Piernas = Area_Pierna * 2
print (f"El área total del muñeco es: {Area_Completa + Area_Brazos + Area_Piernas:.2f}")