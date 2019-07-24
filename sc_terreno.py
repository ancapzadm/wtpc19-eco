import numpy as np

class Terreno(object):
    """Superclase Terreno. Comunica entre sí los objetos de la clase Animal, almacena información de sus posiciones y los administra (inserta, mueve, elimina)."""

    def __init__(self, nfilas, ncolumnas):
        """El constructor de un objeto de la clase Terreno crea array 2D de Numpy 'grilla' con 'nfilas' filas y 'ncolumnas' columnas. Cada celda de la grilla 2D es capaz de contener un único objeto animal; hace referencia a una posición en el espacio del problema."""
        self.grilla = np.empty((nfilas,ncolumnas), dtype=object)

    def insertar(self, animal, posicion_objetivo):
        """Se inserta un objeto 'animal' en una 'posicion_objetivo' (tupla de la forma (fila,columna)) de la grilla 2D del terreno."""
        # Se añade el animal a la 'posicion_objetivo'
        fila_objetivo, columna_objetivo = posicion_objetivo
        self.grilla[fila_objetivo,columna_objetivo] = animal

    def generar_posicion_random(self, animal):
        """Se genera una posición aleatoria (fila,columna) que se encuentre vacía en la grilla del terreno."""
        # Se lee el tamaño de la grilla
        nfilas,ncolumnas = self.grilla.shape
        # Se realiza el proceso hasta que se logre conseguir una posición vacía
        exito = False
        while not exito:
            # Se genera una posición aleatoria
            random_fila = np.random.randint(nfilas)
            random_columna = np.random.randint(ncolumnas)
            # Se controla si la posición está vacía
            if self.grilla[random_fila,random_columna] == None: exito = True
        return (random_fila,random_columna)

    def ubicar(self, animal):
        """Informa la posición que tiene el objeto 'animal' en la grilla 2D, como una tupla (fila,columna)."""
        return tuple(np.argwhere(self.grilla==animal)[0])

    def ubicar_vecinos(self, animal):
        """Se devuelve una lista con los objetos animales vecinos que son visibles (dentro del rango de visión) para el objeto 'animal'."""
        # Lee la posición de 'animal' en la grilla del terreno
        fila_centro,columna_centro = self.ubicar(animal)
        # Lee el rango de visión del 'animal'
        vision_animal = animal.get_vision()
        # Establece límites de visión superior e inferior en las 2D de la grilla del terreno
        fila_min = fila_centro - vision_animal
        fila_max = fila_centro + vision_animal
        columna_min = columna_centro - vision_animal
        columna_max = columna_centro + vision_animal
        # Corrige los límites si caen fuera de la grilla 2D; para ello lee antes el tamaño de la grilla
        nfilas,ncolumnas = self.grilla.shape
        if fila_min < 0: fila_min = 0
        if columna_min < 0: columna_min = 0
        if fila_max >= nfilas: fila_max = nfilas-1 
        if columna_max >= ncolumnas: columna_max = ncolumnas-1
        # Genera una lista de los vecinos que se encuentran en el rango de visión
        vecinos_visibles = self.grilla[fila_min:fila_max+1, columna_min:columna_max+1].flatten()
        return vecinos_visibles

    def eliminar(self, animal):
        """Se elimina el objeto 'animal' de la grilla (queda en su lugar un espacio vacío (None)."""
        # Se obtiene la posición del objeto 'animal' en la grilla
        fila_objetivo,columna_objetivo = self.ubicar(animal)
        # Se sobreescribe la posición con 'None' (borrando el objeto)
        self.grilla[fila_objetivo,columna_objetivo] = None

    def calcular_distancia(posicion_A, posicion_B):
        """Devuelve la distancia en cantidad de casilleros, que existe entre dos posiciones A y B: tuplas de la forma (fila,columna)."""
        fila_A, columna_A = posicion_A
        fila_B, columna_B = posicion_B
        distancia_fila = abs(fila_B-fila_A)
        distancia_columna = abs(columna_B-columna_A)
        return distancia_fila+distancia_columna
"""
    def mover(self, animal, posicion_objetivo):
        Mueve al 'animal' en la grilla 2D hacia la 'posición_objetivo' (tupla de la forma (fila,columna)), sin que ésta exceda su máxima velocidad.
        # Se ubica al 'animal' en la grilla
        posicion_animal = self.ubicar(animal)
        # Se calcula la distancia (en cantidad de pasos) a la 'posicion_objetivo" desde la ubicación del 'animal'
        # Para moverse, el 'animal' trata de acortar la distancia por la componente más extensa, sin exceder su velocidad máxima ni atravesar casillas ocupadas; el 'animal' se detiene al alcanzar su 'posición_objetivo' (excepto que esté ocupada).
        nueva_fila,nueva_columna = posicion_animal
        velocidad_animal = animal.get_velocidad()
        for paso in range(velocidad_animal):
            # Se crea una lista de las posiciones libres alrededor del 'animal' para realizar un paso ([izquierda, derecha, arriba, abajo])
            posiciones_libres = [(nueva_fila-1,nueva_columna),(nueva_fila+1,nueva_columna),(nueva_fila,nueva_columna+1),(nueva_fila,nueva_columna-1)]
            posiciones_libres = [posicion for posicion in posiciones_libres if self.grilla[posicion[0],posicion[1]] == None]
        # Si el animal no está atrapado
        if len(posiciones_libres) != 0:
            # Si sólo hay una posicion libre
            if len(posiciones_libres) == 1:
                # CONTINUAR
            # Procede a eliminar el 'animal' de su posición en la grilla para luego insertarlo en la nueva posición alcanzada"""
