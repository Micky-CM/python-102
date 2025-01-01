# Agregar elementos en una lista
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

# Agregar elementos utilizando list comprehension
numbers_v2 = [element * 2 for element in range(1, 11)]
# Sintaxis: [ elemento   Ciclo donde se extraen elementos de cualquier iterable ]
print(numbers_v2)


# Ejemplo para obtener múltiplos de 3
numbers = []
for i in range(1, 21):
    if i % 3 == 0:
        numbers.append(i)

print(numbers)

# Sintaxis de list comprehension
numbers_v2 = [i for i in range(1,21) if i % 3 == 0]
print(numbers_v2)
