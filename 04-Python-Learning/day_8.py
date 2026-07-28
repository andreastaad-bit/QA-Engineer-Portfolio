dog = {}
dog = {"name":"brown","breed": "dalmation", "legs": 3, "age": 10}
print(dog)

students = {"fisrt_name": "Andrea","last_name": "Velazquez", "gender": "femenino", "age": 27, "marital_status": "widow", "skills": ["cook","embroiderer", "coding", "costumer service"], "country": "Costa rica", "city": "Cahuita","address": "nonja"}
print(len(students))
print(students)


print(students["skills"])
print(type(["skills"]))

students["skills"].append("bilingue")
students["skills"].append("Postman")
print(students["skills"])
print(students)

lista_llaves= students.keys()
print(lista_llaves)

valores_lista=students.values()
print(valores_lista)

print(students.items())
print(students.pop("marital_status"))
print(students)
students["tipo sangre"]=("O +")
print(students)

del dog

