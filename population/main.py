import utils
import read_csv
import charts

def run():
    # Almacena en 'data' la lista de diccionarios del csv señalando la ubicación del archivo
    data = read_csv.read_csv('./population/data.csv')

    # ---- Lógica para graficar el porcentaje de población en los países de Sur América ---- #
    # Filtra solo los países con la llave 'Continent' que sea igual a 'South America'
    data = list(filter(lambda item: item['Continent'] == 'South America',data))

    # Almacena en 'countries' una lista de todos los países de 'data'
    countries = list(map(lambda x: x['Country/Territory'], data))
    # Almacena en 'percentages' una lista de todos los porcentajes de 'data'
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages) # Genera una gráfica con forma de pie

    '''
    # ---- Lógica para graficar la población en todas las gestiones de la base de datos ---- #
    country = input('Type Country: ') # input para que el usuario escriba el nombre del país

    # LLama a la función para obtener la población por país
    result = utils.population_by_country(data, country)

    if len(result) > 0: # Mayor a 0 porque de lo contrario no habría encontrado el país
        country = result[0] # Selecciona el país que encontró de la lista de diccionarios
        labels, values = utils.get_population(country) # Obtiene la poblaciones de los años
        charts.generate_bar_chart(labels, values) # Genera una gráfica de barras
    '''

if __name__ == '__main__':
    run()