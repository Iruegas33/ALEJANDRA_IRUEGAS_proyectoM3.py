PROYECTO MODULO 3. SIMULACIÓN DE LA MAQUINA DE GALTON.
# Simulación de una máquina de Galton de 3000 canicas
# En total tendrá 12 niveles de obstáculos -deberás decidir si va a caer a un lado o al otro 12 veces el resultado final serà un histograma que represente la cantidad de canicas en cada contenedor, como el siguiente 
# No olvides colocar el nombre a los ejes y un título al gráfico.
# Deberás emplear dos funciones: una para calcular los resultados de las canicas y la segunda para la 
# graficación del histograma. 
# No es necesario hacer la animación de las canicas cayendo ni los obstáculos, solamente los contenedores
# con resultados de la simulación. 
# NO debes usar la función normal().

1. Hay que importar las bibliotecas de numpy (matemáticas/numeros aleatorios) y la biblioteca para graficar matplotlib
2. Se divide el problema general en 2 funciones: uno que recree la simulación de la maquina de Galton y otra función que grafique los resultados
3. La función que simula la máquina de galton: mediante dos ciclos for anidados cada canica (de las 3000) por cada nivel (12 en este caso) con una posibilidad del 50% en cada nivel de irse a la derecha o a la izquierda (la misma posibilidad en ambas direcciones) de forma aleatoria
4. lo que conduce a una distribución normal (en estadística), una campana de Gauss.
5. La información se almacena en la lista compartimientos, que guarda el numero de canicas que 'quedaron' en cada compartimiento.
6. La función de la gráfica: se crean los niveles segun el tamaño de 'compartimientos' para crear el eje de las 'x',
7. compartimientos= es el eje de las 'y' (cantidad de canicas). Como se solicita en el problema: se identifican mediante 'label' los ejes de las x y de las y.
8. Se da titulo a la grafica con title. En este caso, las barras serán color rosa. 
9. En el cuerpo principal del programa se declaran las vairables num_canicas y num_niveles (por si se quieren cambiar) y se
10. mandan llamar las dos funciones creadas previamente.
11. La función de canicas_aleatorias tiene como parámetros a num_canicas y num_niveles, y se guarda en 'resultados' para poderlo pasar como parámetro a 
12. La función de grafica_canicas. 

El bootcamp se me ha hecho muy interesante. Sin embargo me gustaría que hubiera más ejemplos, más textos o información concreta donde ampliar conocimientos 
Por otro lado me hubiera gustado que trabajaramos todos en el mismo editor de código para maximizar el aprendizaje del mismo (sacarle todo el provecho que se pueda al editor de código).
Saludos y gracias. 

   
   
