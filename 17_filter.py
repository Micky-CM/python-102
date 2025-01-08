numbers = [1, 2, 3, 4, 5]
# Variable = list(filter(lambda elemento: expresion con condición, lista))
even_numbers = list(filter(lambda num: num % 2 == 0, numbers)) # Filtra los números pares

print(even_numbers)
print(numbers) # 'filter' no afecta a la lista original