# Agregar elementos en un diccionario
dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)

# Agregar elementos utilizando list comprehension
dict_v2 = { i: i * 2 for i in range(1, 5) }
# Sintaxis: {clave: valor   Ciclo donde se extraen elementos de cualquier iterable}
print(dict_v2)


# Ejemplo con diccionario de paises
import random # Importa la librería para obtener números aleatorios

countries = ['col', 'mex', 'bra']

population = {}
for country in countries:
    population[country] = f'{random.randint(10, 100)} M. de hab.'

print(population)

population_v2 = {country: f'{random.randint(10, 100)} M. de hab.' for country in countries}
# Sintaxis: {clave: valor f'iterable con formato'   Ciclo donde se extraen elementos}
print(population_v2)


# Iterar 2 listas para formar un diccionario
names = ['nico', 'zule', 'santi']
ages = [12, 56, 48]

print(list(zip(names, ages))) # Une ambas listas en una lista con tuplas

new_dict = {name: age for (name, age) in zip(names, ages)}
# Sintaxis: {clave: valor Ciclo donde se extraen elementos de unir ambas listas}
print(new_dict)