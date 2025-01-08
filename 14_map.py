numbers = [1, 2, 3, 4]

numbers_v2 = [] # 3 líneas de código para iterar la lista
for num in numbers:
    numbers_v2.append(num * 2)

print(numbers)
print(numbers_v2)

# map realiza una transformación en cada uno de los elementos de la lista
# Se usa 'list()' para visivilizar los cambios en una lista
# Variable = list(map(lambda iterable para map: expresión, listas))
numbers_v3 = list(map(lambda num: num * 2, numbers)) # Una sola línea de código
print(numbers_v3)


numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)

# Variable = list(map(lambda argumentos: expresión, lista1, lista2))
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
# Para transformar los elementos de las listas, toma en cuenta la lista con menor longitud
print(result)