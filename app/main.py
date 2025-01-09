import utils

data = [
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Bolivia',
        'Population': 11
    },
    {
        'Country': 'Brasil',
        'Population': 500
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input('Type Country: ')
    result = utils.population_by_country(data, country)
    print(result)

# Condicional para ejecutar como script desde la terminal o para ser ejecutado desde otro archivo
if __name__ == '__main__': # Muy común en archivos de Python para controlar la dualidad de los mmódulos
    run()