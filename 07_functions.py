print('Hello world') # Función nativa de Python

def my_print(text): # La función my_print solicita un parámetro 'text'
    print('This is my print')
    print(text * 2)

my_print('Hola. ') # Al ejecutar la función se pasa un argumento string 'Hola. '


def suma(a, b): # La función solicita 2 parámetros
    print(a + b)

suma(3, 4) # Se ejecuta la función con 2 argumentos
suma(7.9, 5.8)