import functools # 'reduce' es una función de functools

numbers = [1, 2, 3, 4]

# variable = functools.reduce(lambda contador, elemento: contador + elemento, lista)
result = functools.reduce(lambda counter, item: counter + item, numbers)
print('Suma de los números de la lista:', result)

largest = functools.reduce(max, numbers) # 'max' hace iteraciones y extrae el número mayor
print('Número mayor de la lista:',largest)