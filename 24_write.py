with open('./text.txt', 'r+') as file: # 'r+' le otorga permisos de lectura y escritura
#with open('./text.txt', 'w+') as file: # 'w+' reemplaza el contenido
    for line in file:
        print(line)
    file.write('\nBy Gemini') # Agrega una nueva línea con un salto de línea (/n) al inicio