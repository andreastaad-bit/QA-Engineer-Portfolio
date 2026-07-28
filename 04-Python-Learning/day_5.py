comida = []
print(comida)

comidas_fav = ["Hamburguesas", "Arepas", "Queso", "Quesadillas" , "Sushi", "Pastel"]
print(len(comidas_fav))

com_1,com_2,com_3,com_4,com_5,com_6 = comidas_fav
print(com_1)
print(com_3)
print(com_6)

mixed_data_types = ["Andrea", 27 , 1.65, "Soltera", "Leon,Gto"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
comp1,comp2,comp3,comp4,comp5,comp6,comp7 = it_companies
print(comp1)
print(comp4)
print(comp7)
it_companies[0]= "Instagram"
print(it_companies)
it_companies.append("Twitter")
it_companies.insert(4,"Linux")
print(it_companies)

it_companies[0] = "FACEBOOK"
print(it_companies)

companies_join= "#;".join(it_companies)
print(companies_join)

does_exist = "Linux" in it_companies
print(does_exist)

new_it_companies = sorted(it_companies)
print(new_it_companies)

new_it_companies = sorted(it_companies,reverse=True)
print(new_it_companies)

some_companies = it_companies[0:3]
print(some_companies)

some_new_companies = it_companies[6:]
print(some_new_companies)

print(len(it_companies))

middle = it_companies[4]
print(middle)

del it_companies[0]
print(it_companies)
print(len(it_companies))

del it_companies[3:5]
print(it_companies)
print(len(it_companies))

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

print(it_companies)
print(some_new_companies)

del some_new_companies
del some_companies


print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_and_back_end = front_end + back_end
print(front_and_back_end)

full_stack = front_and_back_end.copy()
print(full_stack)
full_stack.append("SQL")
full_stack.append("Redux")
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

ages.append(19)
ages.append(26)
print(ages)
ages.sort()
print(len(ages))
middle = len(ages)//2
print(middle)
print(ages[5])
print(ages[6])
middle_1 = (ages[middle -1] +ages[middle]) / 2
print(middle_1)

print("Next one")
average = sum(ages) / len(ages)
print(average)
print(max(ages))
print(min(ages))
age_range= (ages[-1] - ages[0])
print(age_range)
distancia_de_min = abs(min(ages) - average)
print(distancia_de_min)
distancia_de_max = abs(max(ages) - average)
print(distancia_de_max)

print("Level 2, Countries exercises")
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
print(len(countries))
middle_countries = len(countries) // 2
print(middle_countries)
print(countries[97])

countries_2 = countries[0:99]
print(countries_2)

countries_3 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country,second_country,third_country,*scandic_countries = countries_3
print(first_country)
print(second_country)
print(third_country)
print(scandic_countries)

