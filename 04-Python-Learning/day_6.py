gatos = ()
print(gatos)

hermanas = ("Arantza","Ana lilia", "Deniss", "Cameron","Yered")
hermanos = ("Andres","Juan","Carlos","Ismael")
print(hermanas)
print(hermanos)

todos_hermanos = hermanas + hermanos
print(todos_hermanos)
print(len(todos_hermanos))

familia = list(todos_hermanos)
print(familia)

familia.append("Gabriela")
familia.append("Juan Jose")
print(sorted(familia))

familia= tuple(familia)
print(familia)

print("Level 2")

familia=list(familia)
print(familia)

p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11 = familia
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)

animales =("vaca","pollo","jirafa","burro","hipopotamo","elefante","puma")
frutas = ("uva","sandia","mango","banana","melón","durazno","manzana","papaya")
vegetales = ("tomate","chayote","calabaza","pepino","lechuga","brocoli","col")

comida_otros_tp = animales + frutas + vegetales
print(comida_otros_tp)

food_stuff_it= list(comida_otros_tp)
print(food_stuff_it)
print(len(food_stuff_it))

middle_item= len(food_stuff_it)//2
print(middle_item)
print(food_stuff_it[11])
print(food_stuff_it[10])

primeros_tres= food_stuff_it[0:3]
ultimos_tres = food_stuff_it[-3:]
print(primeros_tres)
print(ultimos_tres)

food_stuff_it=tuple(food_stuff_it)
print(food_stuff_it)

del food_stuff_it

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
