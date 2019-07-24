class Animal(object):
    """Superclase Animal. Atributos y métodos compartidos por las presas y los predadores."""

    def __init__(self, velocidad, vision, energia_maxima):
        """El constructor inicializa todos los atributos de un objeto de la clase Animal. La 'energia' del animal comienza con un valor equivalente al 100% de su 'energia_maxima' (medida de la constitución del animal)."""
        self.velocidad = velocidad
        self.vision = vision
        self.energia_maxima = energia_maxima
        self.energia = energia_maxima
        self.plan = None

    def get_velocidad(self):
        """'Getter' que devuelve el valor del atributo 'velocidad' del objeto de la superclase Animal. Indica la máxima cantidad de casillas que puede desplazarse un animal al moverse en un paso temporal."""
        return self.velocidad

    def get_vision(self):
        """'Getter' que devuelve el valor del atributo 'vision' del objeto de la superclase Animal. Indica el rango de visión del animal; se traduce a cuántas casillas puede ver a su alrededor desde la posición de la grilla (región cuadrada alrededor del animal)."""
        return self.vision

    def get_energia(self):
        """'Getter' que devuelve el valor del atributo 'energia' del objeto de la superclase Animal. Es una medida de la vitalidad del animal."""
        return self.energia

    def get_plan(self):
        """'Getter' que devuelve el valor del atributo 'plan' del objeto de la superclase Animal. Guarda una tupla cuya primera posición corresponde a una palabra clave que codifique a una acción decidida previamente por el animal como un plan a ejecutar. La segunda posición corresponde a una estructura de formato variable (puede ser complejo) que permite a los métodos ejecutar() de las subclases, realizar la acción planificada."""
        return self.plan

    def get_clase(self):
        """'Getter' que devuelve el nombre de la clase con la que fue creado el objeto de la superclase Animal (Ej.: 'Presa' o 'Predador' si es una de las dos subclases o 'Animal' si se crea directamente desde esa superclase)."""
        return self.__class__.__name__

    def observar(self, terreno):
        """El animal observa a su alrededor. Devuelve una lista con los objetos animales que puede observar desde su posición en la grilla terreno."""
        return terreno.ubicar_vecinos(self)
        
    def modificar_energia(self, valor_porcentual):
        """El animal altera su energía por un valor porcentual (respecto de su energía máxima) que puede ser positivo (para aumentarla) o negativo (para disminuirla). La energía del animal tiene un límite inferior en '0' y uno superior en 'energia_maxima'."""
        self.energia += int((valor_porcentual/100)*self.energia_maxima)

