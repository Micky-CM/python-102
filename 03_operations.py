set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Unión de conjuntos
set_c = set_a.union(set_b) # Método 'union'
print(set_c)

print(set_a | set_b) # Operador '|' que signivica unión

# Intersección
set_c = set_a.intersection(set_b) # Método 'intersection'
print(set_c)

print(set_a & set_b) # Operador '&' que signivica intersección


# Diferencia
set_c = set_a.difference(set_b) # Método 'difference'
print(set_c)

print(set_a - set_b) # Operador '-' que resta de set_a los elementos comunes con set_b

# Diferencia simétrica
set_c = set_a.symmetric_difference(set_b) # Método 'symmetric_difference'
print(set_c)

print(set_a ^ set_b) # Operador '^' que resta solo los elementos comunes entre set_a y set_b
