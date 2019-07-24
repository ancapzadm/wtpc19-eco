##### Proyecto final del Workshop sobre Técnicas de Programación Científica 2019 (WTPC19) - Facultad de Ciencias Químicas, Universidad Nacional de Córdoba, Córdoba, Argentina.
##### Grupo del Proyecto "Ecosistema" ('Eco'): Modelo Basado en Agentes (MBA) que simula la interacción entre predador-presa, implementado en Python3 según el paradigma de programación orientada a objetos (OOP).

###-----------------------------------
### 1) Se importan librerías y clases
import numpy as np
from sc_animal import Animal
from c_presa import Presa
from c_predador import Predador
from sc_terreno import Terreno

if __name__ == "__main__":
    

    terreno = Terreno(10,10)
    animal = Animal(1,1,1)

    
    
    lobo = Predador(1,1,1)
    aux_pos=terreno.generar_posicion_random(lobo)
    
    terreno.insertar(lobo,aux_pos)
    terreno.ubicar(lobo)
    lobo.decidir(terreno)
    print (terreno.grilla)
