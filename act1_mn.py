"""   Autor:
   Argel Jesus Pech Manrique
   argelpech098@gmail.com
   Version 2.0 : 03/02/2025 00:30am
"""

import numpy as np #se importa la libreria a usar para todo el codigo
import matplotlib.pyplot as plt #Importar esta libreria para visualizar los graficos

epsilon = 1.0 #numero inical de epsilon
iteracion = 0 #contador
N_Iteraciones= []#guarda las iteraciones realizadas
Epsilon = []#guarda todos los epsilon calculados
#ciclo para encontrar la precision de la maquina
while 1.0 + epsilon != 1.0:
    epsilon /= 2 # Se divide epsilon por 2 en cada iteración
    iteracion = iteracion + 1 # Se incrementa el contador de iteraciones
    N_Iteraciones.append(iteracion) # Se guarda la iteración actual en la lista
    Epsilon.append(epsilon) # Se guarda el valor de epsilon actual en la lista
    print(f"Iteración: {iteracion}, Precisión de máquina: {epsilon}") # Se imprime la iteración y el valor de epsilon

# Crear la figura para el gráfico
plt.figure()
# Graficar la precisión de la máquina en función de las iteraciones
plt.plot(N_Iteraciones, Epsilon, label='Precisión de máquina', marker='o')
plt.xlabel('Iteración') # Nombre del eje x
plt.ylabel('Epsilon') # Nombre del eje y
plt.title('Precisión de máquina') # Título del gráfico
plt.show() # Mostrar el gráfico

# Se multiplica epsilon por 2 para obtener el último valor válido
epsilon *= 2
print(f"Precisión de máquina: {epsilon}")
