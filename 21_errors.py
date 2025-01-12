#print(0 / 0)) # Sintax Error : un paréntesis está demás
#print(0 / 0) # Zero Division Error : no se puede dividir entre 0
#print(result) #Name Error : 'result' no fue definido

# Cuando se lanza un error o una excepción, el programa se detiene y deja de ejecutarse

suma = lambda x, y: x + y
#assert suma(2, 2) == 5 # Assertion Error : no se cumple la hipótesis
assert suma(2, 2) == 4 # Verifica la hipótesis

# El código se sigue ejecutando después de mostrar el mensaje de error
print('Ejecuntando...')

# Se pueden crear excepciones personalizadas
age = 10
if age < 18:
    raise Exception('No se permite menores de edad')
