set_countries = {'col', 'bol', 'mex', 'bra'}
print(set_countries)

size = len(set_countries) # Cantidad de elementos
print(size)

# Preguntar por un elemento en específico
print('col' in set_countries)
print('pe' in set_countries)

# Agregar elementos 'add'
set_countries.add('pe')
print(set_countries)

# Actualizar un conjunto 'update'
set_countries.update({'arg', 'ecu'})
print(set_countries)

# Eliminar elementos 'remove' y 'discard'
set_countries.remove('pe')
print(set_countries)
set_countries.remove('bra')
print(set_countries)
#set_countries.remove('ven') # Error en consola porque no encuentra el elemento
set_countries.discard('ven') # No ocasiona error y continúa la ejecución del código
print(set_countries)

# Limpiar todos los elementos del conjunto 'clear'
set_countries.clear()
print(set_countries)
