price = 100 # Alcance global

def increment():
    price = 200 # Alcance local
    result = price + 10
    return result

print(price) # Imprime la variable glogal
price_2 = increment()
print(price_2) # Imprime la variable local
#print(result) # La variable result no está definida fuera del contexto de la función