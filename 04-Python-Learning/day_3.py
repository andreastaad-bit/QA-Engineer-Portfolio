import math 



age = 27
height = 166.0
no_mi_edad = 1 + 36j
base = 560
altura = 465
area_triangulo = base * altura / 2
lado_a = 34
lado_b = 67
lado_c = 87
perimetro_triangulo = lado_a + lado_b + lado_c 
largo = 234.5
ancho = 45.6
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
radio = 12.34
area_circulo = 3.24 * radio ** 2
circunferencia = 2 * 3.14 * radio
slope = 2
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = (y2 -y1) / (x2 - x1)
dx = x2 -x1
dy = y2 -y1
distance = math.sqrt(dx ** 2 + dy **2)
largo = len("python")
largo_decimal = float(largo)
largo_str = str(largo_decimal)
numero = 4864
division = 7 // 3
valor = 2.7
valor_convertido = int(valor)
numero_1 = "10"
numero_2 = 10
numero_3 = "9.8"
numero_3_con = float(numero_3)
float_numero_3 = int(numero_3_con)
hora = 40
pago_por_hora = 28
ingreso_semanal = hora * pago_por_hora
años_con_vida = int(input("¿Cuantos años de vida tienes?:"))

segundos_por_año = 365 * 24 *60 *60 
segundos_vividos = años_con_vida * segundos_por_año














print(age)
print(type(age))
print(height)
print(type(height))
print(no_mi_edad)
print(type(no_mi_edad))
print(area_triangulo)
print(perimetro_triangulo)
print(area_rectangulo)
print(perimetro_rectangulo)
print(area_circulo)
print(circunferencia)
print(m)
print(distance)
print(m == distance)

print(len("Python"))
print(len("dragon"))
print(len("Python") != len("dragon"))
print("on" in "Python" and "on"in "dragon")
print("jargon" in "I hope this course is not full of jargon")
print("on" not in "python" and "on" not in "dragon")
print(largo)
print(largo_decimal)
print(largo_str)
print(type(largo_str))
print(numero % 2)
print(numero % 2 == 0)
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero no es par")
print(division)
print(valor_convertido)
print(type(numero_1))
print(type(numero_2))
print(numero_3)
print(numero_3_con)
print(float_numero_3)
print(numero_3_con == 10)
print(ingreso_semanal)
print("has vivido aprox", segundos_vividos, "segundos")

for n in range(1, 6):
    print(n, n**0, n**1, n**2, n**3)