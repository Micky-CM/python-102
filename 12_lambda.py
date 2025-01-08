def increment(x):
    return x + 1

result = increment(7)
print(result)

# Nombre función = 'lambda' argumento : expresiones (return)
increment_v2 = lambda x: x + 1 # 'lambda' palabra reservada de Python
result_v2 = increment_v2(7)
print(result_v2)

# Nombre función = 'lambda' argumentos o parámetros : expresiones
full_name = lambda name, last_name: f'Fullname is {name.title()} {last_name.title()}'

text = full_name('miguel', 'colque')
print(text)
