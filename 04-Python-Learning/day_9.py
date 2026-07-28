age = int(input("Enter you age:"))


if age >= 18:
    print("You are old enough to drive")
else:
    print(f"You need {18 - age} more years to learn to drive")
    
    
print("Exercise 2")


my_age = 27
your_age= int(input("¿Cuál es tu edad?"))

difference = abs(my_age - your_age)


if my_age == your_age:
    print("Tenemos la misam edad")

elif my_age > your_age:
    if difference == 1:
        print(f"Soy mayor que tu por {difference} año")
    else:
        print(f"Soy mayor por {difference} años")
    
else:
    if difference == 1:
        print(f"Eres mayor por {difference} año")
    else:
        print(f"Eres mayor por {difference } años")

print("Exercise 3")

a = int(input("Ingresa un número:"))
b = int(input("Ingresa otro número:"))

if a > b:
    print(f"{a} es más grande que {b}")
elif a == b:
    print(f"{a} es igual que {b}")
else: 
    print(f"{a} es menor que {b}")

print("Exercises: Level 2")
 
calificación=int(input("Cuál es tu calificación:"))


if calificación >=90:
    print("A")
elif calificación >=80:
    print("B")
elif calificación >=70:
    print("C")
elif calificación >=60:
    print("D")
else: 
    print("F")

print("Exercise 2 level 2")


Primavera = ["Marzo","Abril","Mayo"]
Verano = ["Junio", "Julio","Agosto"]
Otoño = ["Septiembre","Octubre","Noviembre"]
Invierno = ["Diciembre","Enero","Febrero"]


mes = input("¿En que mes te encuentras?:").capitalize()


if mes in Verano:
    print("Verano")
elif mes in Primavera:
    print("Primavera")
elif mes in Otoño:
    print("Otoño")
elif mes in Invierno:
    print("Invierno")
else: 
    print("Mes no válido")

print("Exercises: Level 3")

fruits = ["banana","orange","mango","lemon"]

fruit = input("Ingresa una fruta:")

if fruit in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruit)
    print(fruits)


person={
    'first_name': 'Andrea',
    'last_name': 'Velazquez',
    'age': 69,
    'country': 'Mexico',
    'is_married': True,
    'skills': ['Postman', 'MongoDB', 'Python',"JIRA","Pycharm"],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
        }


# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

middle= len("skills")// 2


if "skills"  in person:
    print(person["skills"][middle])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "skills" in person:
    if "Python" in person["skills"]:
        print("Python found")
    else:
        print("Python not found")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 
if "skills" in person:
    skills = person["skills"]

if "JavaScript" in skills and "React" in skills:

     print("He is a front end developer")
elif "Node" in skills and "Python"in skills and "MongoDB" in skills:
    print("He is a backend developer")
elif "React" in skills and "Node" in skills  and "MongoVB" in skills :
    print("He is a fullstack developer")
else:
    print("unknown title")

#If the person is married and if he lives in Mexico, print the information in the following format:
# first and last name lives in Mexico. She is married.
    
first_name = person["first_name"]
last_name = person["last_name"]

if person["is_married"] and person["country"] == "Mexico":
    print(f"{first_name } {last_name} lives in Mexico. She is marreid")
else:
    print("False")


    







      


    