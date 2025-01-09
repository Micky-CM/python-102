'''
from pkg.mod_1 import func_1, func_2 # importa las funciones de la carpeta 'mod_1'
from pkg.mod_2 import func_3, func_4 # importa las funciones de la carpeta 'mod_2'
# Aunque se llame al paquete dos veces, solo se inicia una sola vez

print(func_1())
print(func_2())
print(func_3())
print(func_4())
'''

# Una buena práctica es llamar a un paquete que tenga namescapes para evitar conflictos de funciones que tengan el mismo nombre
import pkg # Es una manera más directa y correcta de llamar paquetes
print(pkg.URL)
print(pkg.mod_1.func_1()) #