##### Proyecto final del Workshop sobre Técnicas de Programación Científica 2019 (WTPC19) - Facultad de Ciencias Químicas, Universidad Nacional de Córdoba, Córdoba, Argentina.
##### Grupo del Proyecto "Ecosistema" ('Eco'): Modelo Basado en Agentes (MBA) que simula la interacción entre predador-presa, implementado en Python3 según el paradigma de programación orientada a objetos (OOP).

###-----------------------------------
### 1) Se importan librerías y clases
import numpy as np
from c_presa import Presa
from c_predador import Predador
from sc_terreno import Terreno

if __name__ == "__main__":

    ### 2) Se establecen los parámetros de simulación
        ## 2.1) Set de parámetros de terreno
        ## 2.2) Set de parámetros para animales
        ## 2.3) Set de parámetros temporales

    ### 3) Se construye un estado inicial
        ### 3.1) Se crean objetos terreno y animales
        ### 3.2) Se insertan animales al terreno
        ### 3.3) Se guarda y/o visualiza el estado inicial

    ### 4) Se ejecuta la simulación
        ### 4.1) Todos los animales deciden un plan de acción
        ### 4.2) Todos los animales ejecutan su plan
            ## 4.2.1) Ejecutan los predadores
            ## 4.2.2) Ejecutan las presas
        ### 4.3) Se guarda y/o visualiza el estado actual
        ### 4.4) Se avanza el paso temporal
