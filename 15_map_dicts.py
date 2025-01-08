items = [ # Lista de diccionarios
    {
        'product': 'shirt',
        'price': 100
    },
    {
        'product': 'pants',
        'price': 200
    },
    {
        'product': 'jacket',
        'price': 350
    }
]

# Variable = list(map(lambda elemento: elemento[índice], lista))
prices = list(map(lambda item: item['price'], items))
print(prices)

# Función para agregar nueva clave y valor a los diccionarios de la lista
def add_taxes(item):
    item['taxes'] = item['price'] * .19 # modifica la referencia en memoria de la lista original
    return item

# Variable = list(map(función, lista))
new_items = list(map(add_taxes, items)) # 'map' realiza los mismos cambios en la lista original
print('New list:', new_items) # Ambas listas fueron afectadas
print('Old list:', items) # Ambas listas fueron afectadas
