#PROYECTO MODULO 3. SIMULACIÓN DE LA MAQUINA DE GALTON.

# Simulación de una máquina de Galton de 3000 canicas
# En total tendrá 12 niveles de obstáculos -deberás decidir si va a caer a un lado o al otro 12 veces
#el resultado final serà un histograma que represente la cantidad de canicas en cada contenedor, como el siguiente 
# No olvides colocar el nombre a los ejes y un título al gráfico.
# Deberás emplear dos funciones: una para calcular los resultados de las canicas y la segunda para la 
# graficación del histograma. 
# No es necesario hacer la animación de las canicas cayendo ni los obstáculos, solamente los contenedores
# con resultados de la simulación. 
# NO debes usar la función normal().

import numpy as np  #importar la biblioteca numèrica/matemática, genera numeros aleatorios
import matplotlib.pyplot as plt # importar biblioteca para crear gráficos/visualizaciones

# Función para calcular los resultados de las canicas
def canicas_aleatorias(num_canicas, num_niveles):
    """Función que simula una maquina de galton

    Args:
        num_canicas (int): Cantidad de canicas que se tirarán
        num_niveles (int): Numero de niveles de la maquina de Galton

    Returns:
        compartimientos (int): cantidad de canicas en cada compartimiento
    """
    # Crear una lista de compartimientos para almacenar el número de canicas en cada compartimiento
    compartimentos = [0] * (num_niveles + 1)
    
    # Con ciclos for cada canica simula el recorrido por cada nivel
    for i in range(num_canicas):
        posicion = 0
        for i in range(num_niveles):
            # La canica se moverá a la derecha con una probabilidad de 0.5 (50%)
            if np.random.rand() > 0.5:
                posicion += 1
        compartimentos[posicion] += 1
        # Se incrementa el conteo en el compartimiento correspondiente

    return compartimentos # lista que contiene el número de canicas en cada compartimiento despues de la simulación de la maquina de Galton

# Función para graficar el histograma.
def grafica_canicas(compartimentos): 
    """Grafica los resultados de la distribuciòn de las canicas en la maquina de Galton
    toma la lista 'compartimientos`que contiene el numero de canicas en cada compartimiento y luego 
    crea una grafica.

    Args:
        compartimentos : recibe la lista compartimientos (cantidad de canicas en cada compartimiento)
        Genera un histograma con la distribuciòn de las canicas
        Se etiqueta el eje de las X como : Distribución de canicas
        Se etiqueta el eje de las y como: Número de canicas
        El título del histograma es: Simulación de una Máquina de Galton
    """
    niveles = range(len(compartimentos)) # range=Crea una lista de numeros en el rango de len(compartimientos)=numero de compartimientos (desde 0 hasta total de compartimientos - 1)
    plt.bar(niveles, compartimentos, color='pink') #función bar para crear histograma (grafica de barras)
    #niveles= eje x (compartimientos), compartimientos = eje y (numero de canicas), color= color de la grafica
    plt.xlabel('Distribución de canicas') # etiqueta eje de las x
    plt.ylabel('Número de Canicas') # etiqueta eje de las y
    plt.title('Simulación de una Máquina de Galton') # Título de la gráfica
    plt.show() # Muestra la gráfica en una ventana nueva (genera visualización)

# Definir parámetros: numero de canicas y los niveles de la mquina de Galton (en este caso 3000 y 12)
num_canicas = 3000 # numero de canicas utilizadas en este programa
num_niveles = 12 # numero de obstáculos en la máquina de Galton

# Mandar llamar a la función canicas_aleatorias para realizar la simulación. 
# El valor devuelto por `canicas_aleatorias`se almacena en 'resultados'
resultados = canicas_aleatorias(num_canicas, num_niveles) #argumentos: num_canicas y num_niveles

# Mandar llamar la función graficas_canicas para graficar los resultados en un histograma, 
# pasa la variable resultados como argumento 
grafica_canicas(resultados)
