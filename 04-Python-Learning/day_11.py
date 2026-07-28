def generador_nombre():
    nombre_pila = "Andrea"
    apellido = "Guerra"
    espacio = " "
    nombre_completo = nombre_pila + espacio + apellido 
    print(nombre_completo)
    
generador_nombre()

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Andrea'))

def greet(name, location):
    print("Hi there", name, "how is the weather in", location)
greet(name="Andrea", location="Mexico") 
my_dict = {"name": "Andrea", "location": "Mexico"}
greet(**my_dict) 

print("Exercises: Day11")

def add_two_numbers(num1,num2):
    total = num2 + num1
    return total
print(add_two_numbers(89,3788))

def area_circulo(total):
    area = 3.1416 * total ** 2
    return area
print(area_circulo(78))
 
      

