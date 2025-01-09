import sys
print(sys.path) # Muestra la ruta donde se encuentra el módulo 'sys'

import re # Módulo para expresiones regulares
text = 'Mi número de telefono es 311 123 121, el código del país es 57, y mi número de la suerte es 8'
result = re.findall('[5-9]+', text) # Busca todos los números que cumplen el criterio
print(result)

import time
timestamp = time.time()
print(timestamp) # Hora actual para la computadora

local = time.localtime()
local_time = time.asctime(local)
print(local_time) # Formato estandar para humanos

import collections
numbers = [1, 2, 1, 3, 1, 4, 21, 2, 1, 3]
counter = collections.Counter(numbers)
print(counter) # Devuelve un diccionario con la frecuencia de aparición de los números
