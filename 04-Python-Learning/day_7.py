nombres = {"Andres","Ana","Deniss"}
print("Existe el nombre de Deniss dentro de nombres?","Deniss" in nombres)

nombres.pop()
print(nombres)

removed_item = nombres.pop()
print(removed_item)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python&dragon)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers&even_numbers)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1 - st2)

print("Exercises : Day 7")

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.update(["Instagram","Twitter","Linux","Acer"])
print(it_companies)
print(it_companies.pop())

print("The difference between remove and discard is that remove shows an Error its not on the set while descard doesnt show an Error even if its not in the set")

print("Exercises: Level 2")
print(A.union(B))
print(A&B)
print(A.issubset(B))
print(A.isdisjoint(B))

c = A | B
print(c)
d = B | A
print(d)

print(A^B)
del A
del B

print("Exercises:Level 3")
edades = set(age)
print(edades)
print(len(edades))
edades = list(age)
print(edades)
print(len(edades))

print("Difference between tuple, list and set: List, []is can change , you can add items, change indexes, remove items. Tupla: ()you cant modify it, cant change indexes. Set:{} unique items, no order, no double items")

phrase = ("I am a teacher and I love to inspire and teach people")

palabras= phrase.split()
print(palabras)
unique_words=set(palabras)
print(unique_words)
print(len(unique_words))
print(len(phrase))
