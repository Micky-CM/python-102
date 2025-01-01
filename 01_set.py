set_countries = {'col', 'bol', 'mex', 'bra'}
print(set_countries) # Se imprimen de manera aleatoria. El órden no importa
print(type(set_countries))

set_numbers = {1, 3, 7, 3, 22} # El set o conjunto no admite duplicados
print(set_numbers) # No repite el número 3

set_types = {8, 'hello', True, 7.5}
print(set_types)

set_from_string = set('hello')
print(set_from_string) # No repite el caracter 'l'

set_from_tuples = set(('abc', 'def', 'ghi', 'def'))
print(set_from_tuples)

numbers = [3, 1, 2, 3, 1, 4, 2, 1]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)