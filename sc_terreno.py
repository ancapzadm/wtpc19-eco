class Terreno(object):
    """Superclase Terreno. Comunica entre sí los objetos de la clase Animal, almacena información de sus posiciones y los administra (inserta, mueve, elimina)."""

    import numpy as np

    def __init__(self, nfilas, ncolumnas):
        """El constructor de un objeto de la clase Terreno crea array 2D de Numpy 'grilla' con 'nfilas' filas y 'ncolumnas' columnas. Cada celda de la grilla 2D es capaz de contener un único objeto animal; hace referencia a una posición en el espacio del problema."""
        self.grilla = self.np.empty((nfilas,ncolumnas), dtype=object)

    def get_animales(self):
        """'Getter' que devuelve una lista con todos los animales (objetos de la superclase Animal o que hereden de ella) presentes en la grilla terreno."""
        animales_grilla = self.grilla.flatten()
        animales_grilla = [animal for animal in animales_grilla if animal != None]
        return animales_grilla

    def get_presas(self):
        """'Getter' que devuelve una lista con todos los animales de la subclase Presa que están presentes en la grilla terreno."""
        presas_grilla = self.get_animales()
        presas_grilla = [presa for presa in presas_grilla if presa.get_clase() == 'Presa']
        return presas_grilla

    def get_predadores(self):
        """'Getter' que devuelve una lista con todos los animales de la subclase Predador que están presentes en la grilla terreno."""
        predadores_grilla = self.get_animales()
        predadores_grilla = [predador for predador in predadores_grilla if predador.get_clase() == 'Predador']
        return predadores_grilla

    def visualizar(self):
        """Devuelve una foto del terreno que corresponde a un array 2D que muestra por casilla un valor 1 para predadores, -1 para presas y 0 cuando está libre."""
        visiones = {}
        def get_clase(animal):
            """Esta función es luego vectorizada para trabajar con arrays. Devuelve el nombre de la clase del objeto 'animal'."""
            if animal != None:
                nombre_clase = animal.get_clase()
                return nombre_clase
        get_clase_v = self.np.vectorize(get_clase)
        # Se traduce la grilla con objetos a una grilla con 0 y nombres de clases (strings)
        foto = self.np.where(self.grilla == None, 0, get_clase_v(self.grilla))
        # Convierte los nombres de clases a valores enteros
        foto = self.np.where(foto == "Predador", 1, foto)
        foto = self.np.where(foto == "Presa", -1, foto)
        # Convierte el array de objetos a uno de enteros 
        foto = foto.astype(int)
        return foto

    def insertar(self, animal, posicion_objetivo):
        """Se inserta un objeto 'animal' en una 'posicion_objetivo' (tupla de la forma (fila,columna)) de la grilla 2D del terreno."""
        # Se añade el animal a la 'posicion_objetivo'
        fila_objetivo, columna_objetivo = posicion_objetivo
        self.grilla[fila_objetivo,columna_objetivo] = animal

    def generar_posicion_random(self):
        """Se genera una posición aleatoria (fila,columna) que se encuentre vacía en la grilla del terreno."""
        # Se lee el tamaño de la grilla
        nfilas,ncolumnas = self.grilla.shape
        # Se realiza el proceso hasta que se logre conseguir una posición vacía
        exito = False
        while not exito:
            # Se genera una posición aleatoria
            random_fila = self.np.random.randint(nfilas)
            random_columna = self.np.random.randint(ncolumnas)
            # Se controla si la posición está vacía
            if self.grilla[random_fila,random_columna] == None: exito = True
        return (random_fila,random_columna)

    def generar_posicion_lejana(self, animal, posicion_evitar):
        """Genera una posición alejada de otra posición, que se encuentre libre y dentro de la grilla 2D."""
        # Obtenemos la posicion y velocidad máxima del animal
        posicion_animal = self.ubicar(animal)
        velocidad_animal = animal.get_velocidad()
        # Convertimos vectores (tuplas) a componentes
        fila_animal, columna_animal = posicion_animal
        fila_evitar, columna_evitar = posicion_evitar
        # Calculamos el signo de cada diferencia
        signo_fila = self.np.sign(fila_evitar-fila_animal)
        signo_columna = self.np.sign(columna_evitar-columna_animal)
        if signo_fila == 0: signo_fila = [-1,1][self.np.random.randint(2)]
        if signo_columna == 0: signo_columna = [-1,1][self.np.random.randint(2)]
        # La posicion lejana está a una velocidad maxima del animal en cada cateto; el signo menos en fila_lejana es por el sistema de coordenadas del sistema (aumenta hacia abajo y a la derecha) 
        fila_lejana = fila_animal - signo_fila * 2*velocidad_animal
        columna_lejana = columna_animal + signo_columna * 2*velocidad_animal
        # La posición lejana generada se corre (o no) una velocidad maxima en x & y de forma azarosa
        fila_lejana += velocidad_animal * ([-1,0,1][self.np.random.randint(3)])
        columna_lejana += velocidad_animal * ([-1,0,1][self.np.random.randint(3)])
        # Corrige la posición por si se cae fuera de la grilla 2D; para ello lee antes el tamaño de la grilla
        nfilas,ncolumnas = self.grilla.shape
        if fila_lejana < 0: fila_lejana = 0
        if columna_lejana < 0: columna_lejana = 0
        if fila_lejana >= nfilas: fila_lejana = nfilas-1 
        if columna_lejana >= ncolumnas: columna_lejana = ncolumnas-1
        # Devuelve la posición lejana como una tupla
        posicion_lejana = (fila_lejana, columna_lejana)
        return posicion_lejana

    def ubicar(self, animal):
        """Informa la posición que tiene el objeto 'animal' en la grilla 2D, como una tupla (fila,columna)."""
        return tuple(self.np.argwhere(self.grilla==animal)[0])

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
        vecinos_visibles = [vecino for vecino in vecinos_visibles if vecino != None]
        # Eliminarse a sí mismo de la lista
        vecinos_visibles.remove(animal)
        return vecinos_visibles

    def eliminar(self, animal):
        """Se elimina el objeto 'animal' de la grilla (queda en su lugar un espacio vacío (None)."""
        # Se obtiene la posición del objeto 'animal' en la grilla
        fila_objetivo,columna_objetivo = self.ubicar(animal)
        # Se sobreescribe la posición con 'None' (borrando el objeto)
        self.grilla[fila_objetivo,columna_objetivo] = None

    def calcular_distancia(self, posicion_A, posicion_B):
        """Devuelve la distancia en cantidad de casilleros, que existe entre dos posiciones A y B: tuplas de la forma (fila,columna)."""
        fila_A, columna_A = posicion_A
        fila_B, columna_B = posicion_B
        distancia_fila = abs(fila_B-fila_A)
        distancia_columna = abs(columna_B-columna_A)
        return distancia_fila+distancia_columna

    def mover(self, animal, posicion_objetivo):
        """Mueve al 'animal' en la grilla 2D hacia la 'posición_objetivo' (tupla de la forma (fila,columna)), sin que ésta exceda su máxima velocidad."""
        import random

        posicion_animal = self.ubicar(animal)
        fila_animal, columna_animal = posicion_animal
        fila_objetivo, columna_objetivo = posicion_objetivo
        fila_nueva, columna_nueva = fila_animal, columna_animal # Esta es la nueva posicion virtual (tentativo)
        velocidad_animal = animal.get_velocidad()

        # Itero para la cantidad de pasos que puedo hacer
        for paso in range(velocidad_animal):
            # Calculo distancia
            distancia_fila = fila_objetivo - fila_nueva
            distancia_columna = columna_objetivo - columna_nueva
            signo_fila = self.np.sign(distancia_fila)
            signo_columna = self.np.sign(distancia_columna)
            distancia_fila = abs(distancia_fila)
            distancia_columna = abs(distancia_columna)    

            # Lista de posibilidades en el movimiento
            posibilidades = []

            # Ordeno las posibilidades por prioridades (acorto la distancia más extensa)
            if distancia_fila != 0 or distancia_columna != 0:
                if distancia_fila > distancia_columna:
                    movimiento_en_fila = (fila_nueva+signo_fila, columna_nueva)                    
                    posibilidades.append(movimiento_en_fila)
                    if distancia_columna != 0:
                        movimiento_en_columna = (fila_nueva, columna_nueva+signo_columna) 
                        posibilidades.append(movimiento_en_columna)
                else:
                    movimiento_en_columna = (fila_nueva, columna_nueva+signo_columna) 
                    posibilidades.append(movimiento_en_columna)
                    if distancia_fila != 0:
                        movimiento_en_fila = (fila_nueva+signo_fila, columna_nueva)
                        posibilidades.append(movimiento_en_fila)

                # En el caso de que las distancias sean iguales, la prioridad de los dos movimientos posibles es asignada al azar
                if distancia_fila == distancia_columna: self.np.random.shuffle(posibilidades)

                # Itero entre las posibilidades: intento moverme a la primera posibilidad siempre que el casillero al cual me muevo esté libre
                for movimiento in posibilidades:
                    fila_movimiento, columna_movimiento = movimiento
                    posicion = self.grilla[fila_movimiento,columna_movimiento]
                    # Esta sección depende de la subclase del animal
                    if animal.get_clase() == "Predador":
                        if posicion == None or posicion.get_clase() == "Presa":
                            fila_nueva = fila_movimiento
                            columna_nueva = columna_movimiento
                            break
                    elif animal.get_clase() == "Presa":
                        if posicion == None:
                            fila_nueva = fila_movimiento
                            columna_nueva = columna_movimiento
                            break

        # Genero la nueva posicion
        nueva_posicion = (fila_nueva, columna_nueva)

        # Muevo el objeto en la grilla
        self.eliminar(animal)
        self.insertar(animal, nueva_posicion)
