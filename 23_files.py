file = open('./text.txt') # Guarda el archivo 'text.txt' en la variable 'file'
#print(file.read()) # Permite leer todo el texto
#print(file.readline()) # Permite leer el texto línea a línea
#print(file.readline())

for line in file: # Itera el archivo para leer línea a línea
    print(line)

file.close()

# Permite abrir y cerrar el archivo automáticamente después de terminar las ejecuciones del for
with open('./text.txt') as file:
    for line in file:
        print(line)