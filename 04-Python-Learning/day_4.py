first_word = "Thiry"
second_word = "Days"
third_word = "Of"
fourth_word = "Python"
space= ' '
full_sentence = first_word + space + second_word + space + third_word + space + fourth_word
w_1 = "Coding"
w_2= "For"
w_3 = "All"
full_sentence_2 = w_1 + space + w_2 + space + w_3
company = "Coding For All"
primera_palabra = company[0:6]
names = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
ultimo_index = len(company)-1
ejercicio = company.split()
acronimo = ejercicio[0][0] + ejercicio[1][0] + ejercicio[2][0] 
titulo = "Python For Everyone"
ejercicio_2 = titulo.split()
acronimo_2 = ejercicio_2[0][0] + ejercicio_2[1][0] + ejercicio_2[2][0]
sentence = 'You cannot end a sentence with because because because is a conjunction'
resultado = sentence[31:54]
ex_30 ='   Coding For All      '
librerias_python =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' - '.join(librerias_python)
radius = 10
area = 3.24 * radius ** 2
a = 8
b = 6




print(full_sentence)
print(full_sentence_2)
print(company)
print(len(company))
print (company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(primera_palabra)
print(company.index("Coding"))
print(company.replace("Coding", "Python"))
print(company.replace("All", "Everyone"))
print(company.split())
print(names.split(", "))
print(company[0])
print(company[-1])
print(ultimo_index)
print(company[10])
print(ejercicio)
print(acronimo)
print(titulo)
print(acronimo_2)
print(company.index("C"))
print(company.index("F"))
print(company.rindex("l"))
print(sentence.index("because"))
print(sentence.rindex("because"))
print(resultado)
print(company.startswith("Coding"))
print(company.endswith("Coding"))
print(ex_30.strip('  '))
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
print(result)
print( "I am enjoying this challenge.\nI just wonder what is next. ")
print("Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki")
print( " The area of the circle with radius {} is {} meters square.".format(radius,area))
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {} ".format(a,b,a-b))
print("{} * {} = {} ".format(a,b,a*b))
print("{} / {} = {}" .format(a,b, a/b))
print("{} % {} = {} ".format(a,b, a%b))
print("{} // {} = {}".format(a,b, a//b))
print("{} ** {} = {}".format(a,b,a **b))


