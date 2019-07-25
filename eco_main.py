##### Proyecto final del Workshop sobre Técnicas de Programación Científica 2019 (WTPC19) - Facultad de Ciencias Químicas, Universidad Nacional de Córdoba, Córdoba, Argentina.
##### Grupo del Proyecto "Ecosistema" ('Eco'): Modelo Basado en Agentes (MBA) que simula la interacción entre predador-presa, implementado en Python3 según el paradigma de programación orientada a objetos (OOP).

###-----------------------------------
### 1) Se importan librerías y clases
## 1.1) Librerías
import matplotlib.pyplot as plt
import time
## 1.2) Clases
from c_presa import Presa
from c_predador import Predador
from sc_terreno import Terreno

if __name__ == "__main__":

    ### 2) Se establecen los parámetros de simulación
    ## 2.1) Set de parámetros de terreno
    n_filas = 100
    n_columnas = 100
    ## 2.2) Set de parámetros para animales
    # 2.2.1) Predadores
    n_predadores = 5
    velocidad_predador = 1
    vision_predador = 10
    energia_maxima_predador = 20
    nutricion_predador = 25
    coste_moverse_predador = 2
    # 2.2.2) Presas
    n_presas = 20
    velocidad_presa = 1
    vision_presa = 10
    energia_maxima_presa = 10
    nutricion_presa = 5
    coste_moverse_presa = 2
    ## 2.3) Set de parámetros temporales
    pasos_temporales = 10

    ### 3) Se construye un estado inicial
    ## 3.1) Se crea el objeto terreno
    terreno = Terreno(n_filas,n_columnas)
    ## 3.2) Se crean e insertan animales al terreno con una posición random
    # 3.2.1) Predadores
    for i in range(n_predadores):
        predador = Predador(velocidad_predador, vision_predador, energia_maxima_predador, nutricion_predador, coste_moverse_predador)
        posicion_random = terreno.generar_posicion_random()
        terreno.insertar(predador, posicion_random)
    # 3.2.2) Presas
    for j in range(n_presas):
        presa = Presa(velocidad_presa, vision_presa, energia_maxima_presa, nutricion_presa, coste_moverse_presa)
        posicion_random = terreno.generar_posicion_random()
        terreno.insertar(presa, posicion_random)    
    ### 3.3) Se visualiza el estado inicial
    #plt.ion()
    plt.imshow(terreno.visualizar())
    plt.show()

    ### 4) Se ejecuta la simulación
"""	for paso in range(pasos_temporales):
		posicion_random = terreno.generar_posicion_random()
		terreno.insertar(oveja, posicion_random)
		plt.imshow(terreno.visualizar())
		plt.show(block=True)
"""
    ### 4.1) Todos los animales deciden un plan de acción
    ### 4.2) Todos los animales ejecutan su plan
        ## 4.2.1) Ejecutan los predadores
        ## 4.2.2) Ejecutan las presas
    ### 4.3) Se guarda y/o visualiza el estado actual
    ### 4.4) Se avanza el paso temporal
