def sum_with_range(min, max):
    print(f"Rango de números: entre {min} y {max}")
    sum = 0
    for x in range(min, max):
        sum += x
    return sum # Retorna el valor resultado de las operaciones

result = sum_with_range(1, 10) # Almacena el retorno en una variable
print(f"Resultado de la suma: {result}")

result =sum_with_range(result, result + 7) # El valor retornado se utiliza como argumento
print(f"Resultado de la suma: {result}")
