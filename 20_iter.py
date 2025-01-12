for i in range(1, 4): # Itera el elemento 'i' en el range
    print(i) # Imprime la iteración

#my_iter = range(1, 4) # Imprime 'range(1, 4)' sin iteración
my_iter = iter(range(1, 4)) # Lo combierte en un iterador
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter)) # Generará un error con la iteración