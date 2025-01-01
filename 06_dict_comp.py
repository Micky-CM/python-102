import random

countries = ['col', 'mex', 'bra']

population = {country: random.randint(10, 100) for country in countries}
# Sintaxis: {clave: valor con iterable      Ciclo donde se extraen elementos}
print(population)

result = {country: population for (country, population) in population.items() if population > 30}
# Sintaxis: {clave: valor   Ciclo donde se extraen elementos con una condicional}
print(result)

text = 'Hola, soy Micky'

vowels = {char: text.count(char) for char in text if char in 'aeiou'}
# {clave: valor(contador) Ciclo donde se extraen elementos con la condicional que sean vocales}
print(vowels)