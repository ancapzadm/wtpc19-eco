# Se importa la superclase de la cual hereda

from sc_animal import Animal
from sc_terreno import Terreno

class Presa(Animal):
    """Subclase Predador que hereda de la superclase Animal."""

    def decidir(self,terreno):

        """Etapa de planificación. Observa el terreno y decide una acción pensando como presa. Si observa un predador, se escapa; caso contrario, se queda quieta y decide pastar."""
        # Localiza a los predadores visibles entre sus vecinos visibles
        vecinos_visibles = terreno.ubicar_vecinos(self)
        predadores_visibles = [vecino for vecino in vecinos_visibles if vecino.get_class() == "Predador"]
        # Si visualiza predadores, calcula su distancia a ellas
        if len(predadores_visibles) != 0:
            distancias_y_vecinos = {}
            for vecino in lista_vecinos:
                distancia = terreno.calcular_distancia(terreno.ubicar(self), terreno_ubicar(vecino))
                distancias_y_vecinos[distancia] = vecino
            # Determina el vecino más cercano
            distancia_menor = min(list(distancias_y_vecinos.keys()))
            vecino_mas_cercano = distancias_y_vecinos[distancia_menor]
            posicion_vecino_mas_cercano = terreno.ubicar(vecino_mas_cercano)
            # Se aleja del predador más próximo
            # CONITINUAR (Se tiene que idear una forma de que elija una posicion lejana dentro de la grilla, que esté vacía, a la cual desea escaparse; debe considerar la posición del predador más próximo para que esto funciones)
            # posicion_lejana = 
            terreno.mover(self, posicion_lejana)
        # Si no visualiza predadores, decide pastar (no se mueve y aumenta su energía)
        else:
            pass
            #self.modificar_energía(valor_porcentual)

    def ejecutar(self,terreno):
        pass
        """Realiza la acción del plan."""
        # Debe modificarse el método decidir() para que guarde la orden de moverse en el atributo plan y luego aquí se intereprete y se ejecute.
    
