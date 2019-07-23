# Grupo ECO - WTPC 2019
# Este es el script que simula un ecosistema con cazador(depredador) y presa

#Importo librerias

import numpy as np

"""
    Defino las clases del ecosistema
"""

class Terreno(object):

    def __init__(self,nx,ny):
        self.grilla = np.array((nx,ny), ndim=2)#que sea un array de 2D
        self.entes = {}

    def insertar(self,animal):
        """inserta los animales en el terreno (inserta el objeto animal en el diccionario entes)"""
#Asocio un id al animal y lo inserto en entes
        id_animal = np.ran.randint(1e6)
        while id_animal in self.entes.keys():
            id_animal = np.ran.randint(1e6)
        self.entes[id_animal] = animal
#Darle ubicación al animal en la grilla
        nx = self.grilla.shape[0]
        ny = self.grilla.shape[1]
        randomx = np.ran.randint(nx)
        randomy = np.ran.randint(ny)
        self.grilla(randomx,randomy)=id_animal#consultar

    def informar_vecinos(self, animal)
        keys = list(self.entes.keys())
        for k in keys:
            if self.entes[k] is animal
                id = k #id del animal que solicitó

    def eliminar(self,tipo,motivo):
        pass

