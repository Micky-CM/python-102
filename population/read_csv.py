import csv # Librería para trabajar con datos csv

def read_csv(path):
    with open(path, 'r') as scvfile:
        reader = csv.reader(scvfile, delimiter=',')
        header = next(reader) # Obtener la primera fila iterando de forma manual
        data = []
        for row in reader:
            iterable = zip(header, row) # 'zip' une 'header' con los 'row' que se va a iterar
            country_dict = {key: value for key, value in iterable} # Dictionary comprehension
            data.append(country_dict) # Lista de diccionarios
        return data

if __name__ == '__main__':
    data = read_csv('./population/data.csv')
    print(data[0]) # Muestra el primer diccionario de la lista 'data'