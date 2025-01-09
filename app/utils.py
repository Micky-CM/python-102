def get_population():
    keys = ['col', 'bol', 'bra']
    values = [300, 11, 500]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result