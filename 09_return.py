def find_volume(length, width, depth):
    return length * width * depth, 'volumen', True # Se pueden retornar varios valores

result, text, boolean = find_volume(10, 15, 8) # Se almacenan en diferentes variables
print(result)
print(text)
print(boolean)