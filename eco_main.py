##### Proyecto final del Workshop sobre Técnicas de Programación Científica 2019 (WTPC19) - Facultad de Ciencias Químicas, Universidad Nacional de Córdoba, Córdoba, Argentina.
##### Grupo del Proyecto "Ecosistema" ('Eco'): Modelo Basado en Agentes (MBA) que simula la interacción entre predador-presa, implementado en Python3 según el paradigma de programación orientada a objetos (OOP).

###-----------------------------------
### 1) Se importan librerías y clases
## 1.1) Librerías
import matplotlib.pyplot as plt
import numpy as np
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
    n_predadores = 4
    velocidad_predador = 3
    vision_predador = 10
    energia_maxima_predador = 20
    nutricion_predador = 25
    coste_moverse_predador = 2
    # 2.2.2) Presas
    n_presas = 10
    velocidad_presa = 1
    vision_presa = 5
    energia_maxima_presa = 10
    nutricion_presa = 5
    coste_moverse_presa = 2
    ## 2.3) Set de parámetros temporales
    pasos_temporales = 50

    ### 3) Se construye un estado inicial
    ## 3.1) Se crea el objeto terreno
    terreno = Terreno(n_filas,n_columnas)
    ## 3.2) Se crean e insertan animales al terreno con una posición random
    # 3.2.0) Título y grilla explícita para el visualizador    
    plt.title('Predadores vs Presa',loc='center')
    plt.grid(color='w', linestyle='-')
    # 3.2.0.1 Con el permiso de los lectores, voy a crear un animal de cada uno para que pueda correr correctamente la visualizacion 
    predador = Predador(velocidad_predador, vision_predador, energia_maxima_predador, nutricion_predador, coste_moverse_predador)
    posicion_random = terreno.generar_posicion_random()
    terreno.insertar(predador, posicion_random)
    presa = Presa(velocidad_presa, vision_presa, energia_maxima_presa, nutricion_presa, coste_moverse_presa)
    posicion_random = terreno.generar_posicion_random()
    terreno.insertar(presa, posicion_random)
    # 3.2.1) Creación de Predadores
    for i in range(n_predadores-1):
        predador = Predador(velocidad_predador, vision_predador, energia_maxima_predador, nutricion_predador, coste_moverse_predador)
        posicion_random = terreno.generar_posicion_random()
        terreno.insertar(predador, posicion_random)
        # 3.2.1.1) Visualización de Creación    
        figura = plt.imshow(terreno.visualizar(predador,presa))
        # La línea de arriba no es una solución elegante; debería estar fuera del iterador (y ser actualizada con set_data() en lugar de recrear el objeto imshow)
        plt.draw()
        plt.pause(0.5) # Pausa de medio segundo para humanos

    # 3.2.2) Creación de Presas
    for j in range(n_presas-1):
        presa = Presa(velocidad_presa, vision_presa, energia_maxima_presa, nutricion_presa, coste_moverse_presa)
        posicion_random = terreno.generar_posicion_random()
        terreno.insertar(presa, posicion_random)
        # 3.2.1.1) Visualización de Creación
        figura = plt.imshow(terreno.visualizar(predador,presa))
        # La línea de arriba no es una solución elegante; debería estar fuera del iterador (y ser actualizada con set_data() en lugar de recrear el objeto imshow)
        plt.draw()
        plt.pause(0.5) # Pausa de medio segundo para humanos
    
    ### 4) Se ejecuta la simulación
    for paso_tiempo in range(pasos_temporales):
        ### 4.1) Todos los animales deciden un plan de acción
        for animal in terreno.get_animales():
            animal.decidir(terreno)
        ### 4.2) Todos los animales ejecutan su plan
        ## 4.2.1) Ejecutan los predadores
        for predador in terreno.get_predadores():
            predador.ejecutar(terreno)
        ## 4.2.2) Ejecutan las presas
        for presa in terreno.get_presas():
            presa.ejecutar(terreno)
        ### 4.3) Se visualiza el estado actual
        grillita = terreno.visualizar(predador,presa)
        figura.set_data(grillita)

        # La línea de arriba no es una solución elegante; debería estar fuera del iterador (y ser actualizada con set_data() en lugar de recrear el objeto imshow)
        plt.draw()
        plt.pause(0.2) # Pausa de medio segundo para humanos
