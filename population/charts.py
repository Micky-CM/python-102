import matplotlib.pyplot as plt # Importa la librería 'Matplotlib' con el alias 'plt'

def generate_bar_chart(labels, values): # Función para generar una gráfica de barras
    fig, ax = plt.subplots() # 'subplots': método para crear múltiples gráficos en una misma figura
    # 'fig': figura, 'ax': coordenadas
    ax.bar(labels, values) # 'bar': Método para graficas en barras
    # coordenadas.gráfica de barras (encabezados, valores)
    plt.show() # Método para mostrar la gráfica

def generate_pie_chart(labels, values): # Función para generar una gráfica circular de pie
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) # 'pie': Método para graficas en forma de pie
    # coordenadas.gráfica de pie (valores, encabezados=encabezados) *sintaxis de la librería
    ax.axis('equal') # 'axis': organizar en el centro, 'equal': forma circular
    plt.show()


if __name__ == '__main__': # Ejecuta el archivo como script desde la terminal
    labels = ['a', 'b', 'c']
    values = [20, 50, 40]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)